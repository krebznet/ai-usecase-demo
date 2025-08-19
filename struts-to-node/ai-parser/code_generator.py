#!/usr/bin/env python3
"""
Code Generator for Struts to React/Node.js Migration

This tool generates React frontend and Node.js backend code from the migration intent
created by the Struts analyzer.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
import argparse
from textwrap import indent

class ReactCodeGenerator:
    """Generates React frontend code from migration intent"""
    
    def __init__(self, migration_intent: Dict[str, Any], output_dir: str):
        self.intent = migration_intent
        self.output_dir = Path(output_dir)
        self.components_dir = self.output_dir / "src" / "components"
        self.pages_dir = self.output_dir / "src" / "pages"
        self.hooks_dir = self.output_dir / "src" / "hooks"
        self.utils_dir = self.output_dir / "src" / "utils"
        
        # Create directories
        for dir_path in [self.components_dir, self.pages_dir, self.hooks_dir, self.utils_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def generate_all(self):
        """Generate all React code"""
        print("⚛️  Generating React frontend code...")
        
        self._generate_package_json()
        self._generate_components()
        self._generate_routing()
        self._generate_validation_schemas()
        self._generate_api_client()
        self._generate_app_component()
        
        print("✅ React frontend generation complete!")
    
    def _generate_package_json(self):
        """Generate package.json with required dependencies"""
        dependencies = {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-router-dom": "^6.8.0",
            "react-hook-form": "^7.43.0",
            "yup": "^1.0.0",
            "@hookform/resolvers": "^2.9.0",
            "axios": "^1.3.0",
            "@tanstack/react-query": "^4.24.0",
            "tailwindcss": "^3.2.0"
        }
        
        dev_dependencies = {
            "@types/react": "^18.0.0",
            "@types/react-dom": "^18.0.0",
            "@vitejs/plugin-react": "^3.1.0",
            "typescript": "^4.9.0",
            "vite": "^4.1.0",
            "autoprefixer": "^10.4.13",
            "postcss": "^8.4.21"
        }
        
        # Add specific libraries based on components
        for component in self.intent.get('react_components', []):
            for lib in component.get('suggested_libraries', []):
                if lib == 'react-select':
                    dependencies['react-select'] = '^5.7.0'
                elif lib == '@tanstack/react-table':
                    dependencies['@tanstack/react-table'] = '^8.7.0'
        
        package_json = {
            "name": "trucklease-pro-frontend",
            "version": "1.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "tsc && vite build",
                "preview": "vite preview",
                "lint": "eslint src --ext ts,tsx"
            },
            "dependencies": dependencies,
            "devDependencies": dev_dependencies
        }
        
        with open(self.output_dir / "package.json", 'w') as f:
            json.dump(package_json, f, indent=2)
    
    def _generate_components(self):
        """Generate React components from JSP analysis"""
        for component_data in self.intent.get('react_components', []):
            self._generate_single_component(component_data)
    
    def _generate_single_component(self, component_data: Dict[str, Any]):
        """Generate a single React component"""
        component_name = component_data['name']
        component_type = component_data['type']
        state_fields = component_data.get('state_fields', [])
        title = component_data.get('title', component_name)
        
        # Generate TypeScript interface for props
        props_interface = self._generate_props_interface(component_name, component_data.get('props', []))
        
        # Generate component based on type
        if component_type == 'form':
            component_code = self._generate_form_component(component_name, component_data)
        else:
            component_code = self._generate_display_component(component_name, component_data)
        
        # Write component file
        file_content = f"""import React from 'react';
import {{ useForm }} from 'react-hook-form';
import {{ yupResolver }} from '@hookform/resolvers/yup';
import * as yup from 'yup';
import {{ useNavigate }} from 'react-router-dom';

{props_interface}

{component_code}

export default {component_name};
"""
        
        component_file = self.pages_dir / f"{component_name}.tsx"
        with open(component_file, 'w') as f:
            f.write(file_content)
        
        print(f"  📄 Generated {component_name}.tsx")
    
    def _generate_props_interface(self, component_name: str, props: List[str]) -> str:
        """Generate TypeScript interface for component props"""
        if not props:
            return f"interface {component_name}Props {{}}"
        
        prop_definitions = []
        for prop in props:
            if prop == 'loading':
                prop_definitions.append('  loading?: boolean;')
            elif prop == 'user':
                prop_definitions.append('  user?: { id: string; name: string; };')
            elif prop == 'onSubmit':
                prop_definitions.append('  onSubmit?: (data: any) => void;')
            elif prop == 'errors':
                prop_definitions.append('  errors?: Record<string, string>;')
            else:
                prop_definitions.append(f'  {prop}?: any;')
        
        return f"""interface {component_name}Props {{
{chr(10).join(prop_definitions)}
}}"""
    
    def _generate_form_component(self, component_name: str, component_data: Dict[str, Any]) -> str:
        """Generate a form component"""
        state_fields = component_data.get('state_fields', [])
        title = component_data.get('title', component_name)
        
        # Generate form schema
        schema_fields = []
        form_fields = []
        
        for field in state_fields:
            # Generate Yup validation
            if field in ['email']:
                schema_fields.append(f"  {field}: yup.string().email('Invalid email').required('{field.title()} is required'),")
            elif field in ['phone']:
                schema_fields.append(f"  {field}: yup.string().matches(/^[\\d\\s\\-\\(\\)\\+\\.]+$/, 'Invalid phone number').required('Phone is required'),")
            elif field in ['ssn']:
                schema_fields.append(f"  {field}: yup.string().matches(/^\\d{{3}}-?\\d{{2}}-?\\d{{4}}$/, 'Invalid SSN format').required('SSN is required'),")
            else:
                schema_fields.append(f"  {field}: yup.string().required('{field.replace('_', ' ').title()} is required'),")
            
            # Generate form field JSX
            field_type = self._determine_field_type(field)
            field_jsx = self._generate_form_field_jsx(field, field_type)
            form_fields.append(field_jsx)
        
        schema = f"""const validationSchema = yup.object({{
{chr(10).join(schema_fields)}
}});"""
        
        form_jsx = chr(10).join(['        ' + field for field in form_fields])
        
        return f"""
{schema}

const {component_name}: React.FC<{component_name}Props> = ({{ onSubmit }}) => {{
  const navigate = useNavigate();
  const {{
    register,
    handleSubmit,
    formState: {{ errors, isSubmitting }}
  }} = useForm({{
    resolver: yupResolver(validationSchema)
  }});

  const onSubmitForm = (data: any) => {{
    if (onSubmit) {{
      onSubmit(data);
    }}
    // Navigate to next step or show success
    console.log('Form submitted:', data);
  }};

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-md">
        <div className="p-6 border-b">
          <h1 className="text-2xl font-bold text-gray-900">{title}</h1>
          <div className="mt-4">
            {{/* Progress bar */}}
          </div>
        </div>
        
        <form onSubmit={{handleSubmit(onSubmitForm)}} className="p-6">
          {{/* Form fields */}}
{form_jsx}
          
          <div className="flex justify-between mt-8">
            <button
              type="button"
              onClick={{() => navigate(-1)}}
              className="px-6 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
            >
              Back
            </button>
            <button
              type="submit"
              disabled={{isSubmitting}}
              className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
            >
              {{isSubmitting ? 'Submitting...' : 'Continue'}}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}};"""
    
    def _generate_display_component(self, component_name: str, component_data: Dict[str, Any]) -> str:
        """Generate a display/welcome component"""
        title = component_data.get('title', component_name)
        
        return f"""
const {component_name}: React.FC<{component_name}Props> = () => {{
  const navigate = useNavigate();

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-md">
        <div className="p-8 text-center">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">{title}</h1>
          <p className="text-gray-600 mb-8">
            Welcome to the TruckLease Pro application system.
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mb-8">
            {{/* Process steps */}}
            <div className="text-center">
              <div className="w-12 h-12 bg-blue-600 text-white rounded-full flex items-center justify-center mx-auto mb-2">1</div>
              <h3 className="font-semibold">Personal Info</h3>
            </div>
            <div className="text-center">
              <div className="w-12 h-12 bg-gray-300 text-gray-600 rounded-full flex items-center justify-center mx-auto mb-2">2</div>
              <h3 className="font-semibold">Vehicle</h3>
            </div>
            <div className="text-center">
              <div className="w-12 h-12 bg-gray-300 text-gray-600 rounded-full flex items-center justify-center mx-auto mb-2">3</div>
              <h3 className="font-semibold">Financial</h3>
            </div>
            <div className="text-center">
              <div className="w-12 h-12 bg-gray-300 text-gray-600 rounded-full flex items-center justify-center mx-auto mb-2">4</div>
              <h3 className="font-semibold">Background</h3>
            </div>
            <div className="text-center">
              <div className="w-12 h-12 bg-gray-300 text-gray-600 rounded-full flex items-center justify-center mx-auto mb-2">5</div>
              <h3 className="font-semibold">Review</h3>
            </div>
          </div>
          
          <button
            onClick={{() => navigate('/applicant-info')}}
            className="px-8 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 text-lg font-semibold"
          >
            Start Application
          </button>
        </div>
      </div>
    </div>
  );
}};"""
    
    def _determine_field_type(self, field_name: str) -> str:
        """Determine HTML input type based on field name"""
        field_name_lower = field_name.lower()
        
        if 'email' in field_name_lower:
            return 'email'
        elif 'phone' in field_name_lower:
            return 'tel'
        elif 'date' in field_name_lower or 'birth' in field_name_lower:
            return 'date'
        elif 'ssn' in field_name_lower:
            return 'text'
        elif 'password' in field_name_lower:
            return 'password'
        elif field_name_lower in ['state', 'licensestate', 'preferredmake']:
            return 'select'
        elif field_name_lower in ['hascdl']:
            return 'checkbox'
        elif 'requirements' in field_name_lower or 'notes' in field_name_lower:
            return 'textarea'
        else:
            return 'text'
    
    def _generate_form_field_jsx(self, field_name: str, field_type: str) -> str:
        """Generate JSX for a single form field"""
        label = field_name.replace('_', ' ').replace('State', ' State').title()
        
        if field_type == 'select':
            if 'state' in field_name.lower():
                options = ['CA', 'TX', 'FL', 'NY']  # Simplified for demo
                return f'''<div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              {label} *
            </label>
            <select
              {{...register('{field_name}')}}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select {label}</option>
              {chr(10).join([f'              <option value="{opt}">{opt}</option>' for opt in options])}
            </select>
            {{errors.{field_name} && <p className="text-red-500 text-sm mt-1">{{errors.{field_name}.message}}</p>}}
          </div>'''
            else:
                return f'''<div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              {label}
            </label>
            <select
              {{...register('{field_name}')}}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select {label}</option>
              {{/* Options populated based on field type */}}
            </select>
            {{errors.{field_name} && <p className="text-red-500 text-sm mt-1">{{errors.{field_name}.message}}</p>}}
          </div>'''
        
        elif field_type == 'checkbox':
            return f'''<div className="mb-4">
            <div className="flex items-center">
              <input
                type="checkbox"
                {{...register('{field_name}')}}
                className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <label className="ml-2 block text-sm text-gray-900">
                {label}
              </label>
            </div>
            {{errors.{field_name} && <p className="text-red-500 text-sm mt-1">{{errors.{field_name}.message}}</p>}}
          </div>'''
        
        elif field_type == 'textarea':
            return f'''<div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              {label}
            </label>
            <textarea
              {{...register('{field_name}')}}
              rows={{3}}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter {label.lower()}..."
            />
            {{errors.{field_name} && <p className="text-red-500 text-sm mt-1">{{errors.{field_name}.message}}</p>}}
          </div>'''
        
        else:
            return f'''<div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              {label} {("*" if field_name in ["firstName", "lastName", "email", "phone", "ssn"] else "")}
            </label>
            <input
              type="{field_type}"
              {{...register('{field_name}')}}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter {label.lower()}"
            />
            {{errors.{field_name} && <p className="text-red-500 text-sm mt-1">{{errors.{field_name}.message}}</p>}}
          </div>'''
    
    def _generate_routing(self):
        """Generate React Router configuration"""
        routes = []
        for route in self.intent.get('routing', []):
            path = route['path']
            component = route['component']
            protected = route.get('protected', False)
            
            if protected:
                routes.append(f'    <Route path="{path}" element={{<ProtectedRoute><{component} /></ProtectedRoute>}} />')
            else:
                routes.append(f'    <Route path="{path}" element={{<{component} />}} />')
        
        # Add home route
        routes.insert(0, '    <Route path="/" element={<Welcome />} />')
        
        imports = []
        for component_data in self.intent.get('react_components', []):
            component_name = component_data['name']
            imports.append(f"import {component_name} from './pages/{component_name}';")
        
        router_content = f"""import React from 'react';
import {{ BrowserRouter as Router, Routes, Route }} from 'react-router-dom';
{chr(10).join(imports)}

const ProtectedRoute: React.FC<{{ children: React.ReactNode }}> = ({{ children }}) => {{
  // Add authentication logic here
  return <div>{{children}}</div>;
}};

const AppRouter: React.FC = () => {{
  return (
    <Router>
      <Routes>
{chr(10).join(routes)}
      </Routes>
    </Router>
  );
}};

export default AppRouter;
"""
        
        with open(self.output_dir / "src" / "AppRouter.tsx", 'w') as f:
            f.write(router_content)
        
        print("  📄 Generated AppRouter.tsx")
    
    def _generate_validation_schemas(self):
        """Generate Yup validation schemas"""
        schemas = {}
        for rule_name, rule_data in self.intent.get('validation_rules', {}).items():
            fields = rule_data.get('fields', [])
            
            schema_fields = []
            for field in fields:
                if field in ['email']:
                    schema_fields.append(f"  {field}: yup.string().email('Invalid email').required('{field.title()} is required'),")
                elif field in ['phone']:
                    schema_fields.append(f"  {field}: yup.string().matches(/^[\\d\\s\\-\\(\\)\\+\\.]+$/, 'Invalid phone number').required('Phone is required'),")
                elif field in ['ssn']:
                    schema_fields.append(f"  {field}: yup.string().matches(/^\\d{{3}}-?\\d{{2}}-?\\d{{4}}$/, 'Invalid SSN format').required('SSN is required'),")
                else:
                    schema_fields.append(f"  {field}: yup.string().required('{field.replace('_', ' ').title()} is required'),")
            
            schema_code = f"""export const {rule_name}Schema = yup.object({{
{chr(10).join(schema_fields)}
}});"""
            schemas[rule_name] = schema_code
        
        # Write validation schemas file
        validation_content = f"""import * as yup from 'yup';

{chr(10).join(schemas.values())}
"""
        
        with open(self.utils_dir / "validationSchemas.ts", 'w') as f:
            f.write(validation_content)
        
        print("  📄 Generated validationSchemas.ts")
    
    def _generate_api_client(self):
        """Generate API client for backend communication"""
        endpoints = []
        for endpoint in self.intent.get('api_endpoints', []):
            path = endpoint['path']
            method = endpoint['method'].lower()
            form_bean = endpoint.get('form_bean', 'data')
            
            function_name = path.replace('/', '').replace('-', '_')
            
            if method == 'post':
                endpoints.append(f"""
export const {function_name} = async (data: any) => {{
  const response = await api.post('{path}', data);
  return response.data;
}};""")
            else:
                endpoints.append(f"""
export const {function_name} = async () => {{
  const response = await api.get('{path}');
  return response.data;
}};""")
        
        api_content = f"""import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:3001/api';

const api = axios.create({{
  baseURL: API_BASE_URL,
  headers: {{
    'Content-Type': 'application/json',
  }},
}});

// Request interceptor for auth tokens
api.interceptors.request.use(
  (config) => {{
    const token = localStorage.getItem('authToken');
    if (token) {{
      config.headers.Authorization = `Bearer ${{token}}`;
    }}
    return config;
  }},
  (error) => {{
    return Promise.reject(error);
  }}
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {{
    if (error.response?.status === 401) {{
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }}
    return Promise.reject(error);
  }}
);
{chr(10).join(endpoints)}

export default api;
"""
        
        with open(self.utils_dir / "api.ts", 'w') as f:
            f.write(api_content)
        
        print("  📄 Generated api.ts")
    
    def _generate_app_component(self):
        """Generate main App component"""
        app_content = """import React from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import AppRouter from './AppRouter';
import './index.css';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <AppRouter />
      </div>
    </QueryClientProvider>
  );
}

export default App;
"""
        
        with open(self.output_dir / "src" / "App.tsx", 'w') as f:
            f.write(app_content)
        
        # Generate basic CSS with Tailwind
        css_content = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  }
}

@layer components {
  .btn {
    @apply px-4 py-2 rounded-md font-medium focus:outline-none focus:ring-2;
  }
  
  .btn-primary {
    @apply bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500;
  }
  
  .btn-secondary {
    @apply bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500;
  }
  
  .form-input {
    @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500;
  }
}
"""
        
        with open(self.output_dir / "src" / "index.css", 'w') as f:
            f.write(css_content)
        
        print("  📄 Generated App.tsx and index.css")

class NodeCodeGenerator:
    """Generates Node.js backend code from migration intent"""
    
    def __init__(self, migration_intent: Dict[str, Any], output_dir: str):
        self.intent = migration_intent
        self.output_dir = Path(output_dir)
        self.routes_dir = self.output_dir / "src" / "routes"
        self.controllers_dir = self.output_dir / "src" / "controllers"
        self.middleware_dir = self.output_dir / "src" / "middleware"
        self.models_dir = self.output_dir / "src" / "models"
        
        # Create directories
        for dir_path in [self.routes_dir, self.controllers_dir, self.middleware_dir, self.models_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def generate_all(self):
        """Generate all Node.js code"""
        print("🚀 Generating Node.js backend code...")
        
        self._generate_package_json()
        self._generate_server()
        self._generate_routes()
        self._generate_controllers()
        self._generate_middleware()
        self._generate_models()
        
        print("✅ Node.js backend generation complete!")
    
    def _generate_package_json(self):
        """Generate package.json for Node.js backend"""
        dependencies = {
            "express": "^4.18.0",
            "cors": "^2.8.5",
            "helmet": "^6.0.0",
            "express-rate-limit": "^6.7.0",
            "express-validator": "^6.14.0",
            "bcryptjs": "^2.4.3",
            "jsonwebtoken": "^9.0.0",
            "dotenv": "^16.0.0",
            "mongoose": "^6.9.0"
        }
        
        dev_dependencies = {
            "@types/node": "^18.0.0",
            "@types/express": "^4.17.0",
            "@types/cors": "^2.8.0",
            "@types/bcryptjs": "^2.4.0",
            "@types/jsonwebtoken": "^9.0.0",
            "typescript": "^4.9.0",
            "ts-node": "^10.9.0",
            "nodemon": "^2.0.0",
            "@typescript-eslint/eslint-plugin": "^5.0.0",
            "@typescript-eslint/parser": "^5.0.0",
            "eslint": "^8.0.0"
        }
        
        package_json = {
            "name": "trucklease-pro-backend",
            "version": "1.0.0",
            "description": "Backend API for TruckLease Pro application",
            "main": "dist/server.js",
            "scripts": {
                "start": "node dist/server.js",
                "dev": "nodemon src/server.ts",
                "build": "tsc",
                "lint": "eslint src --ext .ts"
            },
            "dependencies": dependencies,
            "devDependencies": dev_dependencies
        }
        
        with open(self.output_dir / "package.json", 'w') as f:
            json.dump(package_json, f, indent=2)
    
    def _generate_server(self):
        """Generate main server file"""
        server_content = """import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import dotenv from 'dotenv';

// Import routes
import applicantRoutes from './routes/applicant';
import vehicleRoutes from './routes/vehicle';
import financialRoutes from './routes/financial';
import backgroundRoutes from './routes/background';
import leaseRoutes from './routes/lease';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});
app.use('/api/', limiter);

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// API routes
app.use('/api/applicant', applicantRoutes);
app.use('/api/vehicle', vehicleRoutes);
app.use('/api/financial', financialRoutes);
app.use('/api/background', backgroundRoutes);
app.use('/api/lease', leaseRoutes);

// Global error handler
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err.stack);
  res.status(500).json({
    message: 'Internal server error',
    error: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong!'
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    message: 'Route not found'
  });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📊 Health check: http://localhost:${PORT}/health`);
});
"""
        
        with open(self.output_dir / "src" / "server.ts", 'w') as f:
            f.write(server_content)
        
        print("  📄 Generated server.ts")
    
    def _generate_routes(self):
        """Generate route files from API endpoints"""
        # Group endpoints by domain
        endpoint_groups = {}
        for endpoint in self.intent.get('api_endpoints', []):
            path = endpoint['path']
            domain = path.split('/')[1] if '/' in path else 'general'
            
            if domain not in endpoint_groups:
                endpoint_groups[domain] = []
            endpoint_groups[domain].append(endpoint)
        
        for domain, endpoints in endpoint_groups.items():
            self._generate_route_file(domain, endpoints)
    
    def _generate_route_file(self, domain: str, endpoints: List[Dict[str, Any]]):
        """Generate a single route file"""
        route_imports = ["import { Router } from 'express';"]
        route_imports.append("import { body } from 'express-validator';")
        route_imports.append(f"import * as {domain}Controller from '../controllers/{domain}Controller';")
        route_imports.append("import { validateRequest } from '../middleware/validation';")
        
        routes = ["const router = Router();", ""]
        
        for endpoint in endpoints:
            path = endpoint['path']
            method = endpoint['method'].lower()
            validation_required = endpoint.get('validation_required', False)
            form_bean = endpoint.get('form_bean', '')
            
            # Generate endpoint path (remove domain prefix)
            endpoint_path = path.replace(f"/{domain}", "") or "/"
            
            # Generate validation middleware if needed
            validation_chain = []
            if validation_required and form_bean:
                if 'applicant' in form_bean.lower():
                    validation_chain = [
                        "body('firstName').notEmpty().withMessage('First name is required')",
                        "body('lastName').notEmpty().withMessage('Last name is required')",
                        "body('email').isEmail().withMessage('Valid email is required')",
                        "body('phone').isMobilePhone('any').withMessage('Valid phone number is required')"
                    ]
                elif 'vehicle' in form_bean.lower():
                    validation_chain = [
                        "body('truckType').notEmpty().withMessage('Truck type is required')",
                        "body('trailerType').notEmpty().withMessage('Trailer type is required')"
                    ]
            
            # Generate route definition
            controller_method = endpoint_path.replace('/', '').replace('-', '_') or 'index'
            if controller_method == 'index':
                controller_method = method
            
            if validation_chain:
                validation_str = ",\n  ".join(validation_chain)
                routes.append(f"""router.{method}('{endpoint_path}', [
  {validation_str},
  validateRequest
], {domain}Controller.{controller_method});""")
            else:
                routes.append(f"router.{method}('{endpoint_path}', {domain}Controller.{controller_method});")
            
            routes.append("")
        
        routes.append("export default router;")
        
        route_content = "\n".join(route_imports + [""] + routes)
        
        with open(self.routes_dir / f"{domain}.ts", 'w') as f:
            f.write(route_content)
        
        print(f"  📄 Generated {domain}.ts route")
    
    def _generate_controllers(self):
        """Generate controller files"""
        # Group endpoints by domain for controllers
        endpoint_groups = {}
        for endpoint in self.intent.get('api_endpoints', []):
            path = endpoint['path']
            domain = path.split('/')[1] if '/' in path else 'general'
            
            if domain not in endpoint_groups:
                endpoint_groups[domain] = []
            endpoint_groups[domain].append(endpoint)
        
        for domain, endpoints in endpoint_groups.items():
            self._generate_controller_file(domain, endpoints)
    
    def _generate_controller_file(self, domain: str, endpoints: List[Dict[str, Any]]):
        """Generate a single controller file"""
        controller_imports = [
            "import { Request, Response, NextFunction } from 'express';",
            f"import {{ {domain.capitalize()}Model }} from '../models/{domain}Model';"
        ]
        
        methods = []
        
        for endpoint in endpoints:
            path = endpoint['path']
            method = endpoint['method'].lower()
            form_bean = endpoint.get('form_bean', '')
            responses = endpoint.get('responses', ['success', 'failure'])
            
            endpoint_path = path.replace(f"/{domain}", "") or "/"
            method_name = endpoint_path.replace('/', '').replace('-', '_') or method
            
            if method == 'post':
                method_code = f"""
export const {method_name} = async (req: Request, res: Response, next: NextFunction) => {{
  try {{
    console.log(`Processing {domain} {method_name}:`, req.body);
    
    // Business logic would go here
    const result = await {domain.capitalize()}Model.create(req.body);
    
    // Simulate different response scenarios based on Struts forwards
    const success = Math.random() > 0.1; // 90% success rate for demo
    
    if (success) {{
      res.json({{
        success: true,
        message: '{domain.capitalize()} {method_name} processed successfully',
        data: result,
        nextStep: '{self._get_next_step(endpoint)}'
      }});
    }} else {{
      res.status(400).json({{
        success: false,
        message: 'Processing failed',
        errors: ['Validation failed or business rule violation']
      }});
    }}
  }} catch (error) {{
    console.error(`Error in {domain} {method_name}:`, error);
    next(error);
  }}
}};"""
            else:
                method_code = f"""
export const {method_name} = async (req: Request, res: Response, next: NextFunction) => {{
  try {{
    console.log(`Getting {domain} {method_name}`);
    
    // Fetch data logic would go here
    const result = await {domain.capitalize()}Model.findAll();
    
    res.json({{
      success: true,
      data: result
    }});
  }} catch (error) {{
    console.error(`Error in {domain} {method_name}:`, error);
    next(error);
  }}
}};"""
            
            methods.append(method_code)
        
        controller_content = "\n".join(controller_imports + methods)
        
        with open(self.controllers_dir / f"{domain}Controller.ts", 'w') as f:
            f.write(controller_content)
        
        print(f"  📄 Generated {domain}Controller.ts")
    
    def _get_next_step(self, endpoint: Dict[str, Any]) -> str:
        """Determine next step from endpoint forwards"""
        forwards = endpoint.get('responses', [])
        if 'success' in forwards:
            # Map common forward patterns to next steps
            path = endpoint['path']
            if 'applicant' in path:
                return '/vehicle-preference'
            elif 'vehicle' in path:
                return '/financial-info'
            elif 'financial' in path:
                return '/background-check'
            elif 'background' in path:
                return '/lease-review'
        return '/'
    
    def _generate_middleware(self):
        """Generate middleware files"""
        # Validation middleware
        validation_middleware = """import { Request, Response, NextFunction } from 'express';
import { validationResult } from 'express-validator';

export const validateRequest = (req: Request, res: Response, next: NextFunction) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      message: 'Validation failed',
      errors: errors.array()
    });
  }
  next();
};

export const asyncHandler = (fn: Function) => {
  return (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
};
"""
        
        with open(self.middleware_dir / "validation.ts", 'w') as f:
            f.write(validation_middleware)
        
        # Auth middleware
        auth_middleware = """import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

interface AuthRequest extends Request {
  user?: any;
}

export const authenticateToken = (req: AuthRequest, res: Response, next: NextFunction) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'Access token required'
    });
  }

  jwt.verify(token, process.env.JWT_SECRET || 'your-secret-key', (err, user) => {
    if (err) {
      return res.status(403).json({
        success: false,
        message: 'Invalid or expired token'
      });
    }
    req.user = user;
    next();
  });
};
"""
        
        with open(self.middleware_dir / "auth.ts", 'w') as f:
            f.write(auth_middleware)
        
        print("  📄 Generated middleware files")
    
    def _generate_models(self):
        """Generate model files"""
        # For demo purposes, create simple in-memory models
        # In production, these would connect to a database
        
        models = ['applicant', 'vehicle', 'financial', 'background', 'lease']
        
        for model_name in models:
            model_content = f"""
interface {model_name.capitalize()}Data {{
  id?: string;
  [key: string]: any;
}}

class {model_name.capitalize()}Model {{
  private static data: {model_name.capitalize()}Data[] = [];
  private static nextId = 1;

  static async create(data: {model_name.capitalize()}Data): Promise<{model_name.capitalize()}Data> {{
    const newRecord = {{
      id: this.nextId.toString(),
      ...data,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    }};
    
    this.data.push(newRecord);
    this.nextId++;
    
    return newRecord;
  }}

  static async findById(id: string): Promise<{model_name.capitalize()}Data | undefined> {{
    return this.data.find(record => record.id === id);
  }}

  static async findAll(): Promise<{model_name.capitalize()}Data[]> {{
    return this.data;
  }}

  static async update(id: string, updateData: Partial<{model_name.capitalize()}Data>): Promise<{model_name.capitalize()}Data | null> {{
    const recordIndex = this.data.findIndex(record => record.id === id);
    if (recordIndex === -1) return null;

    this.data[recordIndex] = {{
      ...this.data[recordIndex],
      ...updateData,
      updatedAt: new Date().toISOString()
    }};

    return this.data[recordIndex];
  }}

  static async delete(id: string): Promise<boolean> {{
    const recordIndex = this.data.findIndex(record => record.id === id);
    if (recordIndex === -1) return false;

    this.data.splice(recordIndex, 1);
    return true;
  }}
}}

export {{ {model_name.capitalize()}Model }};
"""
            
            with open(self.models_dir / f"{model_name}Model.ts", 'w') as f:
                f.write(model_content)
        
        print("  📄 Generated model files")

def main():
    parser = argparse.ArgumentParser(description='Generate React/Node.js code from Struts migration intent')
    parser.add_argument('migration_intent_file', help='Path to migration intent JSON file')
    parser.add_argument('--react-output', '-r', default='./generated-code/react-frontend',
                        help='Output directory for React frontend code')
    parser.add_argument('--node-output', '-n', default='./generated-code/node-backend',
                        help='Output directory for Node.js backend code')
    
    args = parser.parse_args()
    
    # Load migration intent
    with open(args.migration_intent_file, 'r') as f:
        migration_intent = json.load(f)
    
    # Generate React frontend
    react_generator = ReactCodeGenerator(migration_intent, args.react_output)
    react_generator.generate_all()
    
    # Generate Node.js backend
    node_generator = NodeCodeGenerator(migration_intent, args.node_output)
    node_generator.generate_all()
    
    print("\n" + "="*60)
    print("🎉 CODE GENERATION COMPLETE!")
    print("="*60)
    print(f"⚛️  React Frontend: {args.react_output}")
    print(f"🚀 Node.js Backend: {args.node_output}")
    print("\nNext Steps:")
    print("1. Navigate to the React directory and run: npm install && npm run dev")
    print("2. Navigate to the Node.js directory and run: npm install && npm run dev")
    print("3. Customize the generated code to match your specific requirements")
    print("4. Connect to your preferred database in the Node.js models")
    print("5. Configure environment variables for both applications")

if __name__ == '__main__':
    main()