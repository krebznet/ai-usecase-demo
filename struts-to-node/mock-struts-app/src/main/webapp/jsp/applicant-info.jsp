<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Personal Information - Truck Lease Application</title>
    <link rel="stylesheet" type="text/css" href="../css/style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>TruckLease Pro Application</h1>
            <div class="progress-bar">
                <div class="progress-step completed">Start</div>
                <div class="progress-step active">Personal</div>
                <div class="progress-step">Vehicle</div>
                <div class="progress-step">Financial</div>
                <div class="progress-step">Background</div>
                <div class="progress-step">Review</div>
            </div>
        </div>
        
        <div class="content">
            <h2>Step 1: Personal Information</h2>
            <p>Please provide your basic information to get started.</p>
            
            <html:form action="/applicantInfo" method="post">
                <html:errors/>
                
                <div class="form-section">
                    <h3>Basic Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="firstName">First Name *</label>
                            <html:text property="firstName" styleId="firstName" styleClass="form-control" maxlength="50"/>
                        </div>
                        <div class="form-group">
                            <label for="lastName">Last Name *</label>
                            <html:text property="lastName" styleId="lastName" styleClass="form-control" maxlength="50"/>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="email">Email Address *</label>
                            <html:text property="email" styleId="email" styleClass="form-control" maxlength="100"/>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <html:text property="phone" styleId="phone" styleClass="form-control" maxlength="20"/>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="ssn">Social Security Number *</label>
                            <html:text property="ssn" styleId="ssn" styleClass="form-control" maxlength="11"/>
                        </div>
                        <div class="form-group">
                            <label for="dateOfBirth">Date of Birth *</label>
                            <html:text property="dateOfBirth" styleId="dateOfBirth" styleClass="form-control" placeholder="MM/DD/YYYY"/>
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>Address Information</h3>
                    <div class="form-group">
                        <label for="address">Street Address *</label>
                        <html:text property="address" styleId="address" styleClass="form-control" maxlength="200"/>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="city">City *</label>
                            <html:text property="city" styleId="city" styleClass="form-control" maxlength="50"/>
                        </div>
                        <div class="form-group">
                            <label for="state">State *</label>
                            <html:select property="state" styleId="state" styleClass="form-control">
                                <html:option value="">Select State</html:option>
                                <html:option value="AL">Alabama</html:option>
                                <html:option value="CA">California</html:option>
                                <html:option value="FL">Florida</html:option>
                                <html:option value="TX">Texas</html:option>
                                <!-- Additional states would be here -->
                            </html:select>
                        </div>
                        <div class="form-group">
                            <label for="zipCode">ZIP Code *</label>
                            <html:text property="zipCode" styleId="zipCode" styleClass="form-control" maxlength="10"/>
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>License Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="licenseNumber">Driver's License Number *</label>
                            <html:text property="licenseNumber" styleId="licenseNumber" styleClass="form-control" maxlength="20"/>
                        </div>
                        <div class="form-group">
                            <label for="licenseState">License State *</label>
                            <html:select property="licenseState" styleId="licenseState" styleClass="form-control">
                                <html:option value="">Select State</html:option>
                                <html:option value="AL">Alabama</html:option>
                                <html:option value="CA">California</html:option>
                                <html:option value="FL">Florida</html:option>
                                <html:option value="TX">Texas</html:option>
                            </html:select>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <html:checkbox property="hasCDL" styleId="hasCDL"/>
                        <label for="hasCDL">I have a valid Commercial Driver's License (CDL)</label>
                    </div>
                </div>
                
                <div class="form-actions">
                    <html:link action="/welcome" styleClass="btn btn-secondary">Back</html:link>
                    <html:submit styleClass="btn btn-primary">Continue to Vehicle Preferences</html:submit>
                </div>
            </html:form>
        </div>
    </div>
</body>
</html>