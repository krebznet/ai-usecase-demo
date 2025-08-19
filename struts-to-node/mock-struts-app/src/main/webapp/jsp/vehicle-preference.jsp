<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Vehicle Preferences - Truck Lease Application</title>
    <link rel="stylesheet" type="text/css" href="../css/style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>TruckLease Pro Application</h1>
            <div class="progress-bar">
                <div class="progress-step completed">Start</div>
                <div class="progress-step completed">Personal</div>
                <div class="progress-step active">Vehicle</div>
                <div class="progress-step">Financial</div>
                <div class="progress-step">Background</div>
                <div class="progress-step">Review</div>
            </div>
        </div>
        
        <div class="content">
            <h2>Step 2: Vehicle Preferences</h2>
            <p>Tell us about the type of tractor-trailer you're looking to lease.</p>
            
            <html:form action="/vehiclePreference" method="post">
                <html:errors/>
                
                <div class="form-section">
                    <h3>Vehicle Type</h3>
                    <div class="form-group">
                        <label>Truck Type *</label>
                        <div class="radio-group">
                            <html:radio property="truckType" value="day_cab" styleId="day_cab"/>
                            <label for="day_cab">Day Cab</label>
                            
                            <html:radio property="truckType" value="sleeper" styleId="sleeper"/>
                            <label for="sleeper">Sleeper Cab</label>
                            
                            <html:radio property="truckType" value="extended_cab" styleId="extended_cab"/>
                            <label for="extended_cab">Extended Cab</label>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="preferredMake">Preferred Make</label>
                            <html:select property="preferredMake" styleId="preferredMake" styleClass="form-control">
                                <html:option value="">No Preference</html:option>
                                <html:option value="freightliner">Freightliner</html:option>
                                <html:option value="peterbilt">Peterbilt</html:option>
                                <html:option value="kenworth">Kenworth</html:option>
                                <html:option value="mack">Mack</html:option>
                                <html:option value="volvo">Volvo</html:option>
                                <html:option value="international">International</html:option>
                            </html:select>
                        </div>
                        <div class="form-group">
                            <label for="maxModelYear">Maximum Model Year</label>
                            <html:select property="maxModelYear" styleId="maxModelYear" styleClass="form-control">
                                <html:option value="">No Preference</html:option>
                                <html:option value="2024">2024 or newer</html:option>
                                <html:option value="2022">2022 or newer</html:option>
                                <html:option value="2020">2020 or newer</html:option>
                                <html:option value="2018">2018 or newer</html:option>
                            </html:select>
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>Trailer Requirements</h3>
                    <div class="form-group">
                        <label>Trailer Type *</label>
                        <div class="radio-group">
                            <html:radio property="trailerType" value="dry_van" styleId="dry_van"/>
                            <label for="dry_van">Dry Van</label>
                            
                            <html:radio property="trailerType" value="refrigerated" styleId="refrigerated"/>
                            <label for="refrigerated">Refrigerated (Reefer)</label>
                            
                            <html:radio property="trailerType" value="flatbed" styleId="flatbed"/>
                            <label for="flatbed">Flatbed</label>
                            
                            <html:radio property="trailerType" value="tanker" styleId="tanker"/>
                            <label for="tanker">Tanker</label>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="trailerLength">Trailer Length</label>
                            <html:select property="trailerLength" styleId="trailerLength" styleClass="form-control">
                                <html:option value="">No Preference</html:option>
                                <html:option value="48">48 feet</html:option>
                                <html:option value="53">53 feet</html:option>
                            </html:select>
                        </div>
                        <div class="form-group">
                            <label for="numberOfTrailers">Number of Trailers</label>
                            <html:select property="numberOfTrailers" styleId="numberOfTrailers" styleClass="form-control">
                                <html:option value="1">1 Trailer</html:option>
                                <html:option value="2">2 Trailers</html:option>
                                <html:option value="3">3+ Trailers</html:option>
                            </html:select>
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>Usage Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="intendedUse">Primary Use *</label>
                            <html:select property="intendedUse" styleId="intendedUse" styleClass="form-control">
                                <html:option value="">Select Primary Use</html:option>
                                <html:option value="long_haul">Long Haul (OTR)</html:option>
                                <html:option value="regional">Regional</html:option>
                                <html:option value="local_delivery">Local Delivery</html:option>
                                <html:option value="specialized">Specialized Transport</html:option>
                            </html:select>
                        </div>
                        <div class="form-group">
                            <label for="milesPerYear">Expected Miles Per Year</label>
                            <html:select property="milesPerYear" styleId="milesPerYear" styleClass="form-control">
                                <html:option value="">Estimate Annual Miles</html:option>
                                <html:option value="50000">Under 50,000</html:option>
                                <html:option value="75000">50,000 - 75,000</html:option>
                                <html:option value="100000">75,000 - 100,000</html:option>
                                <html:option value="125000">100,000 - 125,000</html:option>
                                <html:option value="150000">125,000+</html:option>
                            </html:select>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="specialRequirements">Special Requirements or Features</label>
                        <html:textarea property="specialRequirements" styleId="specialRequirements" styleClass="form-control" rows="3" placeholder="Any specific equipment, features, or requirements..."/>
                    </div>
                </div>
                
                <div class="form-actions">
                    <html:submit property="action" value="back" styleClass="btn btn-secondary">Back</html:submit>
                    <html:submit styleClass="btn btn-primary">Continue to Financial Information</html:submit>
                </div>
            </html:form>
        </div>
    </div>
</body>
</html>