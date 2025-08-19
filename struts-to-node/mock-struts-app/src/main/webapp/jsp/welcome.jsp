<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Welcome - Truck Lease Application</title>
    <link rel="stylesheet" type="text/css" href="../css/style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>TruckLease Pro Application</h1>
            <div class="progress-bar">
                <div class="progress-step active">Start</div>
                <div class="progress-step">Personal</div>
                <div class="progress-step">Vehicle</div>
                <div class="progress-step">Financial</div>
                <div class="progress-step">Background</div>
                <div class="progress-step">Review</div>
            </div>
        </div>
        
        <div class="content">
            <h2>Ready to Get Started?</h2>
            <p>This application will help you secure financing for your commercial tractor-trailer.</p>
            
            <div class="requirements">
                <h3>Before You Begin, Please Have Ready:</h3>
                <ul>
                    <li>Valid driver's license</li>
                    <li>Social security number</li>
                    <li>Employment and income information</li>
                    <li>Banking information</li>
                    <li>Commercial driving record</li>
                </ul>
            </div>
            
            <div class="estimated-time">
                <strong>Estimated Time:</strong> 10-15 minutes
            </div>
            
            <html:form action="/applicantInfo" method="post">
                <div class="form-actions">
                    <html:submit styleClass="btn btn-primary btn-large">
                        Begin Application
                    </html:submit>
                </div>
            </html:form>
        </div>
    </div>
</body>
</html>