package com.trucklease.utils;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

/**
 * Utility class for common validation operations
 */
public class ValidationUtils {
    
    // State to ZIP code prefix mapping for basic validation
    private static final Map<String, String[]> STATE_ZIP_MAP = new HashMap<>();
    
    static {
        STATE_ZIP_MAP.put("CA", new String[]{"900", "901", "902", "903", "904", "905", "906", "907", "908"});
        STATE_ZIP_MAP.put("TX", new String[]{"733", "734", "735", "736", "737", "738", "739", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785"});
        STATE_ZIP_MAP.put("FL", new String[]{"320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339"});
        STATE_ZIP_MAP.put("NY", new String[]{"100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149"});
        // Add more states as needed...
    }
    
    /**
     * Checks if a string is null or empty
     */
    public static boolean isEmpty(String value) {
        return value == null || value.trim().isEmpty();
    }
    
    /**
     * Calculates age from date of birth string (MM/DD/YYYY format)
     */
    public static int calculateAge(String dateOfBirth) {
        try {
            SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy");
            Date birthDate = sdf.parse(dateOfBirth);
            
            Calendar birth = Calendar.getInstance();
            birth.setTime(birthDate);
            
            Calendar today = Calendar.getInstance();
            
            int age = today.get(Calendar.YEAR) - birth.get(Calendar.YEAR);
            
            // Check if birthday hasn't occurred this year yet
            if (today.get(Calendar.DAY_OF_YEAR) < birth.get(Calendar.DAY_OF_YEAR)) {
                age--;
            }
            
            return age;
        } catch (ParseException e) {
            return -1; // Invalid date format
        }
    }
    
    /**
     * Validates state and ZIP code combination
     */
    public static boolean isValidStateZip(String state, String zipCode) {
        if (isEmpty(state) || isEmpty(zipCode)) {
            return false;
        }
        
        String[] validPrefixes = STATE_ZIP_MAP.get(state.toUpperCase());
        if (validPrefixes == null) {
            return true; // Allow unknown states (incomplete mapping)
        }
        
        String zipPrefix = zipCode.length() >= 3 ? zipCode.substring(0, 3) : zipCode;
        
        for (String prefix : validPrefixes) {
            if (zipPrefix.startsWith(prefix)) {
                return true;
            }
        }
        
        return false;
    }
    
    /**
     * Validates email format
     */
    public static boolean isValidEmail(String email) {
        if (isEmpty(email)) {
            return false;
        }
        
        // Simple email validation regex
        return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
    }
    
    /**
     * Validates phone number format
     */
    public static boolean isValidPhone(String phone) {
        if (isEmpty(phone)) {
            return false;
        }
        
        // Remove all non-digit characters
        String digitsOnly = phone.replaceAll("[^0-9]", "");
        
        // US phone numbers should have 10 digits (with optional country code)
        return digitsOnly.length() == 10 || digitsOnly.length() == 11;
    }
    
    /**
     * Validates Social Security Number format
     */
    public static boolean isValidSSN(String ssn) {
        if (isEmpty(ssn)) {
            return false;
        }
        
        String digitsOnly = ssn.replaceAll("[^0-9]", "");
        
        // Must be exactly 9 digits
        if (digitsOnly.length() != 9) {
            return false;
        }
        
        // Check for invalid patterns
        if (digitsOnly.equals("123456789") || 
            digitsOnly.equals("000000000") || 
            digitsOnly.startsWith("666") || 
            digitsOnly.startsWith("900")) {
            return false;
        }
        
        return true;
    }
    
    /**
     * Validates driver's license number (basic format check)
     */
    public static boolean isValidLicenseNumber(String licenseNumber, String state) {
        if (isEmpty(licenseNumber) || isEmpty(state)) {
            return false;
        }
        
        // Basic validation - each state has different formats
        // This is a simplified version
        switch (state.toUpperCase()) {
            case "CA":
                return licenseNumber.matches("^[A-Z]\\d{7}$"); // A1234567
            case "TX":
                return licenseNumber.matches("^\\d{8}$"); // 12345678
            case "FL":
                return licenseNumber.matches("^[A-Z]\\d{12}$"); // A123456789012
            case "NY":
                return licenseNumber.matches("^\\d{9}$"); // 123456789
            default:
                // For other states, just check it's not empty and has reasonable length
                return licenseNumber.length() >= 5 && licenseNumber.length() <= 15;
        }
    }
    
    /**
     * Sanitizes input string by removing potentially harmful characters
     */
    public static String sanitizeInput(String input) {
        if (isEmpty(input)) {
            return input;
        }
        
        // Remove potential SQL injection and XSS characters
        return input.replaceAll("[<>\"'%;()&+]", "");
    }
    
    /**
     * Formats phone number for display (XXX) XXX-XXXX
     */
    public static String formatPhoneNumber(String phone) {
        if (isEmpty(phone)) {
            return phone;
        }
        
        String digitsOnly = phone.replaceAll("[^0-9]", "");
        
        if (digitsOnly.length() == 10) {
            return String.format("(%s) %s-%s", 
                digitsOnly.substring(0, 3),
                digitsOnly.substring(3, 6),
                digitsOnly.substring(6));
        }
        
        return phone; // Return original if not standard format
    }
    
    /**
     * Formats SSN for display XXX-XX-XXXX
     */
    public static String formatSSN(String ssn) {
        if (isEmpty(ssn)) {
            return ssn;
        }
        
        String digitsOnly = ssn.replaceAll("[^0-9]", "");
        
        if (digitsOnly.length() == 9) {
            return String.format("%s-%s-%s", 
                digitsOnly.substring(0, 3),
                digitsOnly.substring(3, 5),
                digitsOnly.substring(5));
        }
        
        return ssn; // Return original if not standard format
    }
}