#!/usr/bin/env python3
"""
Struts-to-Node Migration Demo

This script demonstrates the complete migration process from a Struts application
to modern React/Node.js stack using AI-powered analysis and code generation.
"""

import os
import sys
from pathlib import Path
import subprocess
import json

# Add the ai-parser directory to Python path
sys.path.append(str(Path(__file__).parent / "ai-parser"))

from struts_analyzer import StrutsAnalyzer
from code_generator import ReactCodeGenerator, NodeCodeGenerator

def main():
    """Run the complete migration demo"""
    print("🚛 TruckLease Pro - Struts to React/Node.js Migration Demo")
    print("=" * 60)
    
    # Paths
    struts_app_path = Path(__file__).parent / "mock-struts-app"
    output_dir = Path(__file__).parent / "analysis_output"
    react_output = Path(__file__).parent / "generated-code" / "react-frontend"
    node_output = Path(__file__).parent / "generated-code" / "node-backend"
    
    # Create output directories
    output_dir.mkdir(exist_ok=True)
    
    print(f"📂 Analyzing Struts application at: {struts_app_path}")
    print(f"📂 Output directory: {output_dir}")
    print()
    
    # Step 1: Analyze Struts Application
    print("Step 1: 🔍 Analyzing Struts Application")
    print("-" * 40)
    
    analyzer = StrutsAnalyzer(str(struts_app_path))
    migration_intent = analyzer.analyze()
    
    # Save analysis results
    analyzer.save_analysis(output_dir / "struts_analysis.json")
    analyzer.save_migration_intent(migration_intent, output_dir / "migration_intent.json")
    
    print(f"\n📊 Analysis Summary:")
    print(f"   • Action Mappings: {len(analyzer.action_mappings)}")
    print(f"   • Form Beans: {len(analyzer.form_beans)}")
    print(f"   • JSP Pages: {len(analyzer.jsp_pages)}")
    print()
    
    # Step 2: Generate React Frontend
    print("Step 2: ⚛️  Generating React Frontend")
    print("-" * 40)
    
    react_generator = ReactCodeGenerator(migration_intent.__dict__, str(react_output))
    react_generator.generate_all()
    
    print()
    
    # Step 3: Generate Node.js Backend
    print("Step 3: 🚀 Generating Node.js Backend")
    print("-" * 40)
    
    node_generator = NodeCodeGenerator(migration_intent.__dict__, str(node_output))
    node_generator.generate_all()
    
    print()
    
    # Step 4: Display Results
    print("Step 4: 📋 Migration Results")
    print("-" * 40)
    
    print("✅ Migration Analysis Complete!")
    print(f"📁 Analysis saved to: {output_dir}")
    print(f"⚛️  React app generated at: {react_output}")
    print(f"🚀 Node.js API generated at: {node_output}")
    
    # Show generated file structure
    print("\n📂 Generated File Structure:")
    print("   React Frontend:")
    for root, dirs, files in os.walk(react_output):
        level = root.replace(str(react_output), '').count(os.sep)
        indent = ' ' * 2 * level
        rel_path = os.path.relpath(root, react_output)
        if rel_path != '.':
            print(f"   {indent}📁 {os.path.basename(root)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            if not file.startswith('.'):
                print(f"   {sub_indent}📄 {file}")
    
    print("\n   Node.js Backend:")
    for root, dirs, files in os.walk(node_output):
        level = root.replace(str(node_output), '').count(os.sep)
        indent = ' ' * 2 * level
        rel_path = os.path.relpath(root, node_output)
        if rel_path != '.':
            print(f"   {indent}📁 {os.path.basename(root)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            if not file.startswith('.'):
                print(f"   {sub_indent}📄 {file}")
    
    # Display next steps
    print("\n🎯 Next Steps for Interview Demo:")
    print("-" * 40)
    print("1. Show the original Struts application structure")
    print("   📂 struts-to-node/mock-struts-app/")
    print("   - XML configurations (struts-config.xml, web.xml)")
    print("   - JSP pages with embedded logic")
    print("   - Java Action classes and Form beans")
    
    print("\n2. Demonstrate AI analysis results")
    print("   📄 analysis_output/migration_intent.json")
    print("   - Extracted components and their relationships")
    print("   - Identified state management needs")
    print("   - API endpoints mapped from Actions")
    
    print("\n3. Show generated modern code")
    print("   ⚛️  React components with TypeScript")
    print("   🎨 Tailwind CSS styling")
    print("   🔧 Form validation with Yup")
    print("   🚀 Express.js REST API")
    print("   📊 Type-safe TypeScript backend")
    
    print("\n4. Highlight AI-powered migration benefits:")
    print("   • Automated component extraction")
    print("   • Preserved business logic")
    print("   • Modern best practices applied")
    print("   • Reduced manual migration effort")
    print("   • Consistent code patterns")
    
    print(f"\n🎉 Migration demo complete!")
    print("Ready for interview presentation! 🚀")

def show_migration_comparison():
    """Show before/after comparison"""
    print("\n📊 BEFORE vs AFTER Comparison")
    print("=" * 50)
    
    print("BEFORE (Struts):")
    print("• JSP pages with mixed HTML/Java code")
    print("• XML-based configuration")
    print("• Server-side form validation")
    print("• Monolithic architecture")
    print("• Limited client-side interactivity")
    
    print("\nAFTER (React/Node.js):")
    print("• Component-based React architecture")
    print("• TypeScript for type safety")
    print("• Client-side validation with Yup")
    print("• RESTful API separation")
    print("• Modern responsive UI with Tailwind")
    print("• State management with hooks")

if __name__ == "__main__":
    main()
    show_migration_comparison()