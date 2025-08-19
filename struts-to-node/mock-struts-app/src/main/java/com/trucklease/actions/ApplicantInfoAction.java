package com.trucklease.actions;

import com.trucklease.beans.ApplicantForm;
import com.trucklease.utils.ValidationUtils;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionMessage;
import org.apache.struts.action.ActionMessages;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Action class for handling applicant information form submission
 */
public class ApplicantInfoAction extends Action {
    
    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form,
                                HttpServletRequest request, HttpServletResponse response)
            throws Exception {
        
        ApplicantForm applicantForm = (ApplicantForm) form;
        HttpSession session = request.getSession();
        
        // Log the action for debugging
        System.out.println("ApplicantInfoAction: Processing applicant information");
        System.out.println("Applicant Name: " + applicantForm.getFirstName() + " " + applicantForm.getLastName());
        
        // Additional server-side validation
        ActionMessages errors = new ActionMessages();
        
        // Validate age (must be 21+ for commercial vehicle leasing)
        if (!ValidationUtils.isEmpty(applicantForm.getDateOfBirth())) {
            int age = ValidationUtils.calculateAge(applicantForm.getDateOfBirth());
            if (age < 21) {
                errors.add("dateOfBirth", new ActionMessage("error.age.minimum", "21"));
            } else if (age > 80) {
                errors.add("dateOfBirth", new ActionMessage("error.age.maximum", "80"));
            }
        }
        
        // Validate SSN format and check for test values
        if (!ValidationUtils.isEmpty(applicantForm.getSsn())) {
            String ssn = applicantForm.getSsn().replaceAll("[^0-9]", "");
            if (ssn.equals("123456789") || ssn.equals("000000000") || ssn.startsWith("666")) {
                errors.add("ssn", new ActionMessage("error.ssn.invalid"));
            }
        }
        
        // Validate state/zip combination
        if (!ValidationUtils.isEmpty(applicantForm.getState()) && 
            !ValidationUtils.isEmpty(applicantForm.getZipCode())) {
            if (!ValidationUtils.isValidStateZip(applicantForm.getState(), applicantForm.getZipCode())) {
                errors.add("zipCode", new ActionMessage("error.state.zip.mismatch"));
            }
        }
        
        // If validation errors, return to input form
        if (!errors.isEmpty()) {
            saveErrors(request, errors);
            return mapping.getInputForward();
        }
        
        // Store form data in session for multi-step process
        session.setAttribute("applicantForm", applicantForm);
        
        // Log successful processing
        System.out.println("ApplicantInfoAction: Successfully processed applicant information");
        
        // Create audit trail entry
        String auditMessage = String.format("Applicant info collected for: %s %s (Email: %s)", 
            applicantForm.getFirstName(), applicantForm.getLastName(), applicantForm.getEmail());
        session.setAttribute("auditTrail", 
            session.getAttribute("auditTrail") + "\n" + auditMessage);
        
        // Forward to next step - vehicle preferences
        return mapping.findForward("success");
    }
}