#!/usr/bin/env python3
"""
Display the migration analysis results in a readable format
"""

import json
from pathlib import Path

def show_migration_intent():
    """Display the migration intent results"""
    analysis_file = Path(__file__).parent / "analysis_output" / "migration_intent.json"
    
    if not analysis_file.exists():
        print("❌ Migration intent file not found. Please run demo.py first.")
        return
    
    with open(analysis_file, 'r') as f:
        intent = json.load(f)
    
    print("🎯 STRUTS-TO-NODE MIGRATION INTENT")
    print("=" * 50)
    
    # React Components
    print("\n⚛️  REACT COMPONENTS")
    print("-" * 30)
    for component in intent.get('react_components', []):
        print(f"📄 {component['name']}")
        print(f"   Type: {component['type']}")
        print(f"   Source: {component['source_file']}")
        print(f"   State Fields: {', '.join(component['state_fields']) if component['state_fields'] else 'None'}")
        print(f"   Validation Required: {'✅' if component['validation_required'] else '❌'}")
        if component.get('suggested_libraries'):
            print(f"   Suggested Libraries: {', '.join(component['suggested_libraries'])}")
        print()
    
    # API Endpoints
    print("🚀 API ENDPOINTS")
    print("-" * 30)
    for endpoint in intent.get('api_endpoints', []):
        print(f"🔗 {endpoint['method']} {endpoint['path']}")
        print(f"   Source Action: {endpoint['source_action']}")
        if endpoint.get('form_bean'):
            print(f"   Form Bean: {endpoint['form_bean']}")
        print(f"   Validation: {'✅' if endpoint['validation_required'] else '❌'}")
        print(f"   Responses: {', '.join(endpoint['responses'])}")
        if endpoint.get('suggested_middleware'):
            print(f"   Middleware: {', '.join(endpoint['suggested_middleware'])}")
        print()
    
    # State Management
    print("🗂️  STATE MANAGEMENT")
    print("-" * 30)
    state_mgmt = intent.get('state_management', {})
    print(f"📊 Recommended Solution: {state_mgmt.get('recommended_solution', 'N/A')}")
    print(f"🔐 Session Management: {state_mgmt.get('session_management', 'N/A')}")
    print(f"📝 Form State: {state_mgmt.get('form_state', 'N/A')}")
    if state_mgmt.get('global_state_entities'):
        print(f"🌐 Global Entities: {', '.join(state_mgmt['global_state_entities'])}")
    print()
    
    # Routing
    print("🗺️  ROUTING")
    print("-" * 30)
    for route in intent.get('routing', []):
        print(f"🛣️  {route['path']} → {route['component']}")
        print(f"   Protected: {'🔒' if route['protected'] else '🔓'}")
        if route.get('redirect_rules'):
            print(f"   Redirects: {route['redirect_rules']}")
        print()
    
    # Validation Rules
    print("✅ VALIDATION RULES")
    print("-" * 30)
    for rule_name, rule_data in intent.get('validation_rules', {}).items():
        print(f"📋 {rule_name}")
        if rule_data.get('fields'):
            print(f"   Fields: {', '.join(rule_data['fields'])}")
        if rule_data.get('rules'):
            print(f"   Rules: {', '.join(rule_data['rules'])}")
        print(f"   Library: {rule_data.get('suggested_library', 'none')}")
        print()

def show_struts_analysis():
    """Display the raw Struts analysis"""
    analysis_file = Path(__file__).parent / "analysis_output" / "struts_analysis.json"
    
    if not analysis_file.exists():
        print("❌ Struts analysis file not found. Please run demo.py first.")
        return
    
    with open(analysis_file, 'r') as f:
        analysis = json.load(f)
    
    print("\n📊 STRUTS APPLICATION ANALYSIS")
    print("=" * 50)
    
    # Action Mappings
    print("\n🎬 ACTION MAPPINGS")
    print("-" * 30)
    for action in analysis.get('action_mappings', []):
        print(f"⚡ {action['path']}")
        print(f"   Class: {action['type']}")
        print(f"   Form: {action.get('name', 'N/A')}")
        print(f"   Validation: {'✅' if action['validate'] else '❌'}")
        if action.get('forwards'):
            print(f"   Forwards: {action['forwards']}")
        print()
    
    # Form Beans
    print("📝 FORM BEANS")
    print("-" * 30)
    for bean in analysis.get('form_beans', []):
        print(f"📋 {bean['name']}")
        print(f"   Class: {bean['type']}")
        if bean.get('properties'):
            print(f"   Properties: {', '.join(bean['properties'])}")
        if bean.get('validations'):
            print(f"   Validations: {', '.join(bean['validations'])}")
        print()
    
    # JSP Pages
    print("📄 JSP PAGES")
    print("-" * 30)
    for jsp in analysis.get('jsp_pages', []):
        print(f"🖼️  {jsp['path']}")
        print(f"   Title: {jsp['title']}")
        if jsp.get('forms'):
            print(f"   Forms: {', '.join(jsp['forms'])}")
        if jsp.get('inputs'):
            input_types = [inp['type'] for inp in jsp['inputs']]
            print(f"   Input Types: {', '.join(set(input_types))}")
        if jsp.get('business_logic'):
            print(f"   Logic: {', '.join(jsp['business_logic'])}")
        print()

def main():
    """Main function"""
    print("🔍 STRUTS-TO-NODE MIGRATION ANALYSIS")
    print("=" * 60)
    
    show_migration_intent()
    show_struts_analysis()
    
    print("\n" + "=" * 60)
    print("📁 Analysis files are saved in: analysis_output/")
    print("⚛️  Generated React code is in: generated-code/react-frontend/")
    print("🚀 Generated Node.js code is in: generated-code/node-backend/")

if __name__ == "__main__":
    main()