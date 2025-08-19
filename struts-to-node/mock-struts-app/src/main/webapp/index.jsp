<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Truck Lease Onboarding System</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to TruckLease Pro</h1>
        <div class="hero-section">
            <h2>Start Your Tractor-Trailer Lease Journey</h2>
            <p>Get approved for your commercial vehicle lease in 5 simple steps</p>
            
            <div class="process-steps">
                <div class="step">
                    <span class="step-number">1</span>
                    <h3>Personal Information</h3>
                    <p>Basic details and contact info</p>
                </div>
                <div class="step">
                    <span class="step-number">2</span>
                    <h3>Vehicle Preference</h3>
                    <p>Choose your ideal truck specifications</p>
                </div>
                <div class="step">
                    <span class="step-number">3</span>
                    <h3>Financial Details</h3>
                    <p>Income and credit information</p>
                </div>
                <div class="step">
                    <span class="step-number">4</span>
                    <h3>Background Check</h3>
                    <p>Authorization for verification</p>
                </div>
                <div class="step">
                    <span class="step-number">5</span>
                    <h3>Lease Agreement</h3>
                    <p>Review and sign your contract</p>
                </div>
            </div>
            
            <div class="action-buttons">
                <html:link action="/welcome" styleClass="btn btn-primary">
                    Start Application
                </html:link>
            </div>
        </div>
    </div>
</body>
</html>