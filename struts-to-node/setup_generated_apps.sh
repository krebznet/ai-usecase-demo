#!/bin/bash

# Setup script for generated React and Node.js applications
# This script prepares the generated code for running

set -e

echo "🚛 TruckLease Pro - Setting up Generated Applications"
echo "===================================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo

# Setup React Frontend
echo "⚛️  Setting up React Frontend..."
echo "--------------------------------"

REACT_DIR="./generated-code/react-frontend"

if [ -d "$REACT_DIR" ]; then
    cd "$REACT_DIR"
    
    # Install dependencies
    echo "📦 Installing React dependencies..."
    npm install
    
    # Add some additional development dependencies if needed
    echo "📦 Installing additional dev dependencies..."
    npm install --save-dev @types/node @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint
    
    # Create a simple index.html for development
    cat > public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="TruckLease Pro - Tractor-Trailer Leasing Application" />
    <title>TruckLease Pro</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
EOF
    
    # Create main.tsx entry point
    cat > src/main.tsx << 'EOF'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
EOF
    
    # Create basic TypeScript config
    cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
EOF
    
    # Create Vite config
    cat > vite.config.ts << 'EOF'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  }
})
EOF
    
    # Create Tailwind config
    cat > tailwind.config.js << 'EOF'
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOF
    
    # Create PostCSS config
    cat > postcss.config.js << 'EOF'
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
EOF
    
    echo "✅ React frontend setup complete!"
    cd ../..
else
    echo "❌ React frontend directory not found. Please run demo.py first."
    exit 1
fi

echo

# Setup Node.js Backend
echo "🚀 Setting up Node.js Backend..."
echo "--------------------------------"

NODE_DIR="./generated-code/node-backend"

if [ -d "$NODE_DIR" ]; then
    cd "$NODE_DIR"
    
    # Install dependencies
    echo "📦 Installing Node.js dependencies..."
    npm install
    
    # Create TypeScript config
    cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020"],
    "module": "commonjs",
    "skipLibCheck": true,
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": false,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist"
  ]
}
EOF
    
    # Create environment file
    cat > .env << 'EOF'
NODE_ENV=development
PORT=3001
FRONTEND_URL=http://localhost:3000
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
EOF
    
    # Create nodemon config
    cat > nodemon.json << 'EOF'
{
  "watch": ["src"],
  "ext": "ts",
  "ignore": ["src/**/*.spec.ts"],
  "exec": "ts-node src/server.ts"
}
EOF
    
    echo "✅ Node.js backend setup complete!"
    cd ../..
else
    echo "❌ Node.js backend directory not found. Please run demo.py first."
    exit 1
fi

echo
echo "🎉 Setup Complete!"
echo "=================="
echo
echo "🚀 To start the applications:"
echo
echo "1. Start the Node.js backend:"
echo "   cd generated-code/node-backend"
echo "   npm run dev"
echo
echo "2. In a new terminal, start the React frontend:"
echo "   cd generated-code/react-frontend"
echo "   npm run dev"
echo
echo "📱 The React app will open at: http://localhost:3000"
echo "🔌 The API server will run at: http://localhost:3001"
echo
echo "📋 Available scripts:"
echo "   • React: npm run dev, npm run build, npm run preview"
echo "   • Node.js: npm run dev, npm run build, npm start"
echo
echo "🎯 Interview Demo Tips:"
echo "   • Show the original Struts code in mock-struts-app/"
echo "   • Demonstrate the analysis results with: python3 show_analysis.py"
echo "   • Compare the generated modern code with the original JSP/Java"
echo "   • Highlight the AI-powered migration benefits"
echo
echo "✨ Ready for your interview presentation!"