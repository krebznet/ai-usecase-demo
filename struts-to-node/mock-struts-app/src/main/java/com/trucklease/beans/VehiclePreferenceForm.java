package com.trucklease.beans;

import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionErrors;
import org.apache.struts.action.ActionMessage;

import javax.servlet.http.HttpServletRequest;

/**
 * Form bean for collecting vehicle preference information
 */
public class VehiclePreferenceForm extends ActionForm {
    
    // Truck Information
    private String truckType;
    private String preferredMake;
    private String maxModelYear;
    
    // Trailer Information
    private String trailerType;
    private String trailerLength;
    private String numberOfTrailers;
    
    // Usage Information
    private String intendedUse;
    private String milesPerYear;
    private String specialRequirements;
    
    @Override
    public ActionErrors validate(ActionMapping mapping, HttpServletRequest request) {
        ActionErrors errors = new ActionErrors();
        
        // Validate required fields
        if (isEmpty(truckType)) {
            errors.add("truckType", new ActionMessage("error.required", "Truck Type"));
        }
        
        if (isEmpty(trailerType)) {
            errors.add("trailerType", new ActionMessage("error.required", "Trailer Type"));
        }
        
        if (isEmpty(intendedUse)) {
            errors.add("intendedUse", new ActionMessage("error.required", "Primary Use"));
        }
        
        // Validate numberOfTrailers is numeric
        if (!isEmpty(numberOfTrailers)) {
            try {
                int trailers = Integer.parseInt(numberOfTrailers);
                if (trailers < 1 || trailers > 10) {
                    errors.add("numberOfTrailers", new ActionMessage("error.range", "Number of Trailers", "1", "10"));
                }
            } catch (NumberFormatException e) {
                errors.add("numberOfTrailers", new ActionMessage("error.invalid", "Number of Trailers"));
            }
        }
        
        return errors;
    }
    
    private boolean isEmpty(String value) {
        return value == null || value.trim().isEmpty();
    }
    
    @Override
    public void reset(ActionMapping mapping, HttpServletRequest request) {
        truckType = null;
        preferredMake = null;
        maxModelYear = null;
        trailerType = null;
        trailerLength = null;
        numberOfTrailers = "1"; // Default to 1 trailer
        intendedUse = null;
        milesPerYear = null;
        specialRequirements = null;
    }
    
    // Getters and Setters
    public String getTruckType() { return truckType; }
    public void setTruckType(String truckType) { this.truckType = truckType; }
    
    public String getPreferredMake() { return preferredMake; }
    public void setPreferredMake(String preferredMake) { this.preferredMake = preferredMake; }
    
    public String getMaxModelYear() { return maxModelYear; }
    public void setMaxModelYear(String maxModelYear) { this.maxModelYear = maxModelYear; }
    
    public String getTrailerType() { return trailerType; }
    public void setTrailerType(String trailerType) { this.trailerType = trailerType; }
    
    public String getTrailerLength() { return trailerLength; }
    public void setTrailerLength(String trailerLength) { this.trailerLength = trailerLength; }
    
    public String getNumberOfTrailers() { return numberOfTrailers; }
    public void setNumberOfTrailers(String numberOfTrailers) { this.numberOfTrailers = numberOfTrailers; }
    
    public String getIntendedUse() { return intendedUse; }
    public void setIntendedUse(String intendedUse) { this.intendedUse = intendedUse; }
    
    public String getMilesPerYear() { return milesPerYear; }
    public void setMilesPerYear(String milesPerYear) { this.milesPerYear = milesPerYear; }
    
    public String getSpecialRequirements() { return specialRequirements; }
    public void setSpecialRequirements(String specialRequirements) { this.specialRequirements = specialRequirements; }
}