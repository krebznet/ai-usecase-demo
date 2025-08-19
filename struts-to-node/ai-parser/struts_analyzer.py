#!/usr/bin/env python3
"""
AI-powered Struts to Modern Web Stack Migration Analyzer

This tool parses Struts applications and generates migration intent for converting
legacy Struts applications to modern React/Node.js architecture.
"""

import re
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path
import argparse

@dataclass
class ActionMapping:
    """Represents a Struts action mapping"""
    path: str
    type: str
    name: Optional[str]
    scope: Optional[str]
    validate: bool
    input: Optional[str]
    forwards: Dict[str, str]
    
@dataclass
class FormBean:
    """Represents a Struts form bean"""
    name: str
    type: str
    properties: List[str]
    validations: List[str]

@dataclass
class JSPPage:
    """Represents a JSP page with extracted components"""
    path: str
    title: str
    forms: List[str]
    inputs: List[Dict[str, str]]
    navigation: List[str]
    business_logic: List[str]

@dataclass
class MigrationIntent:
    """Generated migration plan"""
    react_components: List[Dict[str, Any]]
    api_endpoints: List[Dict[str, Any]]
    state_management: Dict[str, Any]
    routing: List[Dict[str, str]]
    validation_rules: Dict[str, Any]

class StrutsAnalyzer:
    """Main analyzer class for Struts applications"""
    
    def __init__(self, struts_app_path: str):
        self.app_path = Path(struts_app_path)
        self.config_path = self.app_path / "src/main/webapp/WEB-INF"
        self.jsp_path = self.app_path / "src/main/webapp/jsp"
        self.java_path = self.app_path / "src/main/java"
        
        self.action_mappings: List[ActionMapping] = []
        self.form_beans: List[FormBean] = []
        self.jsp_pages: List[JSPPage] = []
        
    def analyze(self) -> MigrationIntent:
        """Main analysis method"""
        print("🔍 Analyzing Struts application...")
        
        # Parse XML configurations
        self._parse_struts_config()
        self._parse_web_xml()
        
        # Analyze JSP pages
        self._analyze_jsp_pages()
        
        # Analyze Java classes
        self._analyze_java_classes()
        
        # Generate migration intent
        migration_intent = self._generate_migration_intent()
        
        print("✅ Analysis complete!")
        return migration_intent
    
    def _parse_struts_config(self):
        """Parse struts-config.xml"""
        config_file = self.config_path / "struts-config.xml"
        if not config_file.exists():
            print(f"⚠️  struts-config.xml not found at {config_file}")
            return
            
        print(f"📄 Parsing {config_file}")
        tree = ET.parse(config_file)
        root = tree.getroot()
        
        # Parse form beans
        form_beans = root.find('form-beans')
        if form_beans is not None:
            for form_bean in form_beans.findall('form-bean'):
                bean = FormBean(
                    name=form_bean.get('name', ''),
                    type=form_bean.get('type', ''),
                    properties=[],
                    validations=[]
                )
                self.form_beans.append(bean)
        
        # Parse action mappings
        action_mappings = root.find('action-mappings')
        if action_mappings is not None:
            for action in action_mappings.findall('action'):
                forwards = {}
                for forward in action.findall('forward'):
                    forwards[forward.get('name', '')] = forward.get('path', '')
                
                mapping = ActionMapping(
                    path=action.get('path', ''),
                    type=action.get('type', ''),
                    name=action.get('name'),
                    scope=action.get('scope'),
                    validate=action.get('validate', 'false').lower() == 'true',
                    input=action.get('input'),
                    forwards=forwards
                )
                self.action_mappings.append(mapping)
    
    def _parse_web_xml(self):
        """Parse web.xml for servlet mappings"""
        web_xml = self.config_path / "web.xml"
        if not web_xml.exists():
            return
            
        print(f"📄 Parsing {web_xml}")
        # Basic web.xml parsing for servlet mappings
        # This could be extended for more complex configurations
    
    def _analyze_jsp_pages(self):
        """Analyze JSP pages to extract UI components and logic"""
        if not self.jsp_path.exists():
            return
            
        print(f"📄 Analyzing JSP pages in {self.jsp_path}")
        
        for jsp_file in self.jsp_path.glob("**/*.jsp"):
            print(f"  - Analyzing {jsp_file.name}")
            
            with open(jsp_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = title_match.group(1) if title_match else jsp_file.stem
            
            # Extract form elements
            forms = re.findall(r'<html:form[^>]*action="([^"]*)"', content)
            
            # Extract input fields
            inputs = []
            input_patterns = [
                r'<html:text[^>]*property="([^"]*)"[^>]*(?:styleClass="([^"]*)")?',
                r'<html:select[^>]*property="([^"]*)"[^>]*(?:styleClass="([^"]*)")?',
                r'<html:checkbox[^>]*property="([^"]*)"[^>]*(?:styleClass="([^"]*)")?',
                r'<html:textarea[^>]*property="([^"]*)"[^>]*(?:styleClass="([^"]*)")?',
                r'<html:radio[^>]*property="([^"]*)"[^>]*(?:value="([^"]*)")?'
            ]
            
            for pattern in input_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        prop_name = match[0]
                        css_class = match[1] if len(match) > 1 else ''
                    else:
                        prop_name = match
                        css_class = ''
                    
                    # Determine input type from pattern
                    input_type = 'text'
                    if 'select' in pattern:
                        input_type = 'select'
                    elif 'checkbox' in pattern:
                        input_type = 'checkbox'
                    elif 'textarea' in pattern:
                        input_type = 'textarea'
                    elif 'radio' in pattern:
                        input_type = 'radio'
                    
                    inputs.append({
                        'property': prop_name,
                        'type': input_type,
                        'cssClass': css_class
                    })
            
            # Extract navigation/links
            navigation = re.findall(r'<html:link[^>]*action="([^"]*)"', content)
            navigation.extend(re.findall(r'<html:submit[^>]*value="([^"]*)"', content))
            
            # Extract business logic indicators
            business_logic = []
            if '<logic:' in content:
                business_logic.append('conditional_logic')
            if '<bean:' in content:
                business_logic.append('data_display')
            if 'session.getAttribute' in content:
                business_logic.append('session_management')
            
            jsp_page = JSPPage(
                path=str(jsp_file.relative_to(self.app_path)),
                title=title,
                forms=forms,
                inputs=inputs,
                navigation=navigation,
                business_logic=business_logic
            )
            self.jsp_pages.append(jsp_page)
    
    def _analyze_java_classes(self):
        """Analyze Java Action classes and Form beans"""
        if not self.java_path.exists():
            return
            
        print(f"📄 Analyzing Java classes in {self.java_path}")
        
        for java_file in self.java_path.glob("**/*.java"):
            print(f"  - Analyzing {java_file.name}")
            
            with open(java_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract class information
            class_match = re.search(r'public class (\w+)', content)
            if not class_match:
                continue
                
            class_name = class_match.group(1)
            
            # Analyze form beans
            if 'extends ActionForm' in content:
                properties = re.findall(r'private\s+\w+\s+(\w+);', content)
                validations = []
                
                # Look for validation logic
                if 'validate(' in content:
                    validations.append('server_side_validation')
                if 'ActionErrors' in content:
                    validations.append('error_handling')
                if 'Pattern.compile' in content:
                    validations.append('regex_validation')
                
                # Update form bean with discovered properties
                for form_bean in self.form_beans:
                    if class_name in form_bean.type:
                        form_bean.properties = properties
                        form_bean.validations = validations
            
            # Analyze action classes
            if 'extends Action' in content:
                # Extract business logic patterns
                if 'session.setAttribute' in content:
                    pass  # Session management logic
                if 'database' in content.lower() or 'dao' in content.lower():
                    pass  # Database operations
    
    def _generate_migration_intent(self) -> MigrationIntent:
        """Generate migration intent based on analysis"""
        print("🎯 Generating migration intent...")
        
        # Generate React components from JSP pages
        react_components = []
        for jsp in self.jsp_pages:
            component_name = self._jsp_to_component_name(jsp.path)
            
            # Determine component type
            component_type = 'form' if jsp.forms else 'display'
            
            # Extract state requirements
            state_fields = [inp['property'] for inp in jsp.inputs]
            
            react_components.append({
                'name': component_name,
                'type': component_type,
                'source_file': jsp.path,
                'title': jsp.title,
                'state_fields': state_fields,
                'validation_required': any(bean.validations for bean in self.form_beans),
                'props': self._extract_component_props(jsp),
                'suggested_libraries': self._suggest_react_libraries(jsp)
            })
        
        # Generate API endpoints from Action mappings
        api_endpoints = []
        for action in self.action_mappings:
            endpoint = {
                'path': action.path.replace('.do', ''),
                'method': 'POST' if action.validate else 'GET',
                'source_action': action.type,
                'form_bean': action.name,
                'validation_required': action.validate,
                'responses': list(action.forwards.keys()),
                'suggested_middleware': self._suggest_node_middleware(action)
            }
            api_endpoints.append(endpoint)
        
        # Generate state management recommendations
        state_management = {
            'recommended_solution': 'Redux Toolkit' if len(self.form_beans) > 3 else 'React Context',
            'session_management': 'JWT tokens',
            'form_state': 'React Hook Form',
            'global_state_entities': [bean.name for bean in self.form_beans]
        }
        
        # Generate routing
        routing = []
        for action in self.action_mappings:
            route = {
                'path': action.path.replace('.do', ''),
                'component': self._action_to_component_name(action.path),
                'protected': action.validate,
                'redirect_rules': action.forwards
            }
            routing.append(route)
        
        # Generate validation rules
        validation_rules = {}
        for bean in self.form_beans:
            if bean.validations:
                validation_rules[bean.name] = {
                    'fields': bean.properties,
                    'rules': bean.validations,
                    'suggested_library': 'Yup' if bean.validations else 'none'
                }
        
        return MigrationIntent(
            react_components=react_components,
            api_endpoints=api_endpoints,
            state_management=state_management,
            routing=routing,
            validation_rules=validation_rules
        )
    
    def _jsp_to_component_name(self, jsp_path: str) -> str:
        """Convert JSP file path to React component name"""
        filename = Path(jsp_path).stem
        # Convert kebab-case to PascalCase
        return ''.join(word.capitalize() for word in filename.replace('-', '_').split('_'))
    
    def _action_to_component_name(self, action_path: str) -> str:
        """Convert action path to component name"""
        name = action_path.lstrip('/')
        return ''.join(word.capitalize() for word in name.split('-'))
    
    def _extract_component_props(self, jsp: JSPPage) -> List[str]:
        """Extract potential props for React component"""
        props = []
        if 'conditional_logic' in jsp.business_logic:
            props.append('loading')
        if 'session_management' in jsp.business_logic:
            props.append('user')
        if jsp.forms:
            props.append('onSubmit')
            props.append('errors')
        return props
    
    def _suggest_react_libraries(self, jsp: JSPPage) -> List[str]:
        """Suggest React libraries based on JSP features"""
        libraries = []
        if jsp.inputs:
            libraries.append('react-hook-form')
        if any(inp['type'] == 'select' for inp in jsp.inputs):
            libraries.append('react-select')
        if 'data_display' in jsp.business_logic:
            libraries.append('@tanstack/react-table')
        return libraries
    
    def _suggest_node_middleware(self, action: ActionMapping) -> List[str]:
        """Suggest Node.js middleware based on action characteristics"""
        middleware = []
        if action.validate:
            middleware.append('express-validator')
        if action.scope == 'session':
            middleware.append('express-session')
        middleware.append('cors')
        return middleware
    
    def save_analysis(self, output_path: str):
        """Save analysis results to JSON file"""
        analysis_data = {
            'action_mappings': [asdict(action) for action in self.action_mappings],
            'form_beans': [asdict(bean) for bean in self.form_beans],
            'jsp_pages': [asdict(jsp) for jsp in self.jsp_pages]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        
        print(f"📁 Analysis saved to {output_path}")
    
    def save_migration_intent(self, migration_intent: MigrationIntent, output_path: str):
        """Save migration intent to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(asdict(migration_intent), f, indent=2, ensure_ascii=False)
        
        print(f"🎯 Migration intent saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Analyze Struts application for migration')
    parser.add_argument('struts_path', help='Path to Struts application directory')
    parser.add_argument('--output-dir', '-o', default='./analysis_output',
                        help='Output directory for analysis results')
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Analyze Struts application
    analyzer = StrutsAnalyzer(args.struts_path)
    migration_intent = analyzer.analyze()
    
    # Save results
    analyzer.save_analysis(output_dir / 'struts_analysis.json')
    analyzer.save_migration_intent(migration_intent, output_dir / 'migration_intent.json')
    
    # Print summary
    print("\n" + "="*50)
    print("📊 MIGRATION ANALYSIS SUMMARY")
    print("="*50)
    print(f"🔧 Action Mappings Found: {len(analyzer.action_mappings)}")
    print(f"📝 Form Beans Found: {len(analyzer.form_beans)}")
    print(f"📄 JSP Pages Found: {len(analyzer.jsp_pages)}")
    print(f"⚛️  React Components to Create: {len(migration_intent.react_components)}")
    print(f"🚀 API Endpoints to Implement: {len(migration_intent.api_endpoints)}")
    print(f"🗂️  State Management: {migration_intent.state_management['recommended_solution']}")
    print(f"✅ Validation Rules: {len(migration_intent.validation_rules)}")
    
    print(f"\n📁 Results saved in: {output_dir}")
    print("🎉 Analysis complete! Ready for migration code generation.")

if __name__ == '__main__':
    main()