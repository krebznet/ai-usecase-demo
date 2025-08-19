package com.trucklease.beans;

import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionErrors;
import org.apache.struts.action.ActionMessage;

import javax.servlet.http.HttpServletRequest;
import java.util.regex.Pattern;

/**
 * Form bean for collecting applicant personal information
 */
public class ApplicantForm extends ActionForm {
    
    // Basic Information
    private String firstName;
    private String lastName;
    private String email;
    private String phone;
    private String ssn;
    private String dateOfBirth;
    
    // Address Information
    private String address;
    private String city;
    private String state;
    private String zipCode;
    
    // License Information
    private String licenseNumber;
    private String licenseState;
    private boolean hasCDL;
    
    // Email validation pattern
    private static final Pattern EMAIL_PATTERN = Pattern.compile(
        "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$"
    );
    
    // Phone validation pattern
    private static final Pattern PHONE_PATTERN = Pattern.compile(
        "^[\\d\\s\\-\\(\\)\\+\\.]{10,}$"
    );
    
    // SSN validation pattern (XXX-XX-XXXX or XXXXXXXXX)
    private static final Pattern SSN_PATTERN = Pattern.compile(
        "^\\d{3}-?\\d{2}-?\\d{4}$"
    );
    
    @Override
    public ActionErrors validate(ActionMapping mapping, HttpServletRequest request) {
        ActionErrors errors = new ActionErrors();
        
        // Validate required fields
        if (isEmpty(firstName)) {
            errors.add("firstName", new ActionMessage("error.required", "First Name"));
        }
        
        if (isEmpty(lastName)) {
            errors.add("lastName", new ActionMessage("error.required", "Last Name"));
        }
        
        if (isEmpty(email)) {
            errors.add("email", new ActionMessage("error.required", "Email Address"));
        } else if (!EMAIL_PATTERN.matcher(email).matches()) {
            errors.add("email", new ActionMessage("error.invalid", "Email Address"));
        }
        
        if (isEmpty(phone)) {
            errors.add("phone", new ActionMessage("error.required", "Phone Number"));
        } else if (!PHONE_PATTERN.matcher(phone).matches()) {
            errors.add("phone", new ActionMessage("error.invalid", "Phone Number"));
        }
        
        if (isEmpty(ssn)) {
            errors.add("ssn", new ActionMessage("error.required", "Social Security Number"));
        } else if (!SSN_PATTERN.matcher(ssn).matches()) {
            errors.add("ssn", new ActionMessage("error.invalid", "Social Security Number"));
        }
        
        if (isEmpty(dateOfBirth)) {
            errors.add("dateOfBirth", new ActionMessage("error.required", "Date of Birth"));
        }
        
        if (isEmpty(address)) {
            errors.add("address", new ActionMessage("error.required", "Address"));
        }
        
        if (isEmpty(city)) {
            errors.add("city", new ActionMessage("error.required", "City"));
        }
        
        if (isEmpty(state)) {
            errors.add("state", new ActionMessage("error.required", "State"));
        }
        
        if (isEmpty(zipCode)) {
            errors.add("zipCode", new ActionMessage("error.required", "ZIP Code"));
        }
        
        if (isEmpty(licenseNumber)) {
            errors.add("licenseNumber", new ActionMessage("error.required", "Driver's License Number"));
        }
        
        if (isEmpty(licenseState)) {
            errors.add("licenseState", new ActionMessage("error.required", "License State"));
        }
        
        return errors;
    }
    
    private boolean isEmpty(String value) {
        return value == null || value.trim().isEmpty();
    }
    
    @Override
    public void reset(ActionMapping mapping, HttpServletRequest request) {
        firstName = null;
        lastName = null;
        email = null;
        phone = null;
        ssn = null;
        dateOfBirth = null;
        address = null;
        city = null;
        state = null;
        zipCode = null;
        licenseNumber = null;
        licenseState = null;
        hasCDL = false;
    }
    
    // Getters and Setters
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    
    public String getSsn() { return ssn; }
    public void setSsn(String ssn) { this.ssn = ssn; }
    
    public String getDateOfBirth() { return dateOfBirth; }
    public void setDateOfBirth(String dateOfBirth) { this.dateOfBirth = dateOfBirth; }
    
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    
    public String getZipCode() { return zipCode; }
    public void setZipCode(String zipCode) { this.zipCode = zipCode; }
    
    public String getLicenseNumber() { return licenseNumber; }
    public void setLicenseNumber(String licenseNumber) { this.licenseNumber = licenseNumber; }
    
    public String getLicenseState() { return licenseState; }
    public void setLicenseState(String licenseState) { this.licenseState = licenseState; }
    
    public boolean getHasCDL() { return hasCDL; }
    public void setHasCDL(boolean hasCDL) { this.hasCDL = hasCDL; }
}