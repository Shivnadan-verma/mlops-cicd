# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Model accuracy: {acc:.4f}")

    joblib.dump(model, "model.joblib")
    print("Model saved to model.joblib")

if __name__ == "__main__":
    train_and_save_model()
“Sympcare”
A Major Project Report

Submitted in Partial Fulfillment of requirements for the Award of Degree of Bachelor of Engineering in Computer Science & Engineering
Submitted to
 
RAJIV GANDHI PROUDYOGIKI VISHWAVIDYALAYA, BHOPAL (M.P)	
Submitted By
Shivnandan Verma (0537AL221029)
Rishiraj Hadge (0537AL221020)
Dinesh Verma (0537AL221012)
Aman Dehariya (0537AL221002)
Under the guidance of
Dr. Priyanka Bhatele
 
DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
SAGAR INSTITUTE OF SCIENCE, TECHNOLOGY & RESEARCH, BHOPAL
Session: Dec 2025 
 
SAGAR INSTITUTE OF SCIENCE, TECHNOLOGY & RESEARCH, BHOPAL
Department of Computer Science & Engineering


 

CERTIFICATE


This is to certify that the project entitled “Sympcare” submitted to Rajiv Gandhi Proudhyogiki Vishwavidyalaya, Bhopal (M.P.) by Mr. Rishiraj Hadge (0537AL221020), Mr. Dinesh Verma (0537AL221012), Mr. Shivnandan Verma (0537AL221029), Mr. Aman Dehariya (0537AL221002) is a partial fulfillment of the requirement for the award of degree of bachelor of Technology in Computer Science & Engineering. The matter embodied is the actual work done Mr. Rishiraj Hadge (0537AL221020), Mr. Dinesh Verma (0537AL221012), Mr. Shivnandan Verma (0537AL221029), Mr. Aman Dehariya (0537AL221002)and is a record of bonafide work done by his/her under my supervision.











Dr. Priyanka Bhatele
          (Guide)	    Dr. Priyanka Bhatele
          (HOD, AIML)	Dr. Jyoti Deshmukh
(Principal)


SAGAR INSTITUTE OF SCIENCE, TECHNOLOGY & RESEARCH, BHOPAL
Department of Computer Science & Engineering


 

APPROVAL CERTIFICATE


This Minor project work entitled “Sympcare” being submitted byMr. Rishiraj Hadge (0537AL221020),Mr. Dinesh Verma (0537AL221012),Mr. Shivnandan Verma (0537AL221029),Mr. Aman Dehariya (0537AL221002)are approved for the award of degree of Bachelor of Engineering in Computer Science and Engineering.

















Internal Examiner                                                              External Examiner

Date:                                                                                   Date:




SAGAR INSTITUTE OF SCIENCE, TECHNOLOGY & RESEARCH, BHOPAL

Department of Computer Science & Engineering


 
CANDIDATE DECLARATION


We Mr. Rishiraj Hadge (0537AL221020), Mr. Dinesh Verma (0537AL221012), Mr. Shivnandan Verma (0537AL221029), Mr. Aman Dehariya (0537AL221002),students of Bachelor of Engineering in Computer Science & Engineering Sagar Institute of Science, Technology & Research, Bhopal (M.P.), hereby declare that the work presented in this Minor project “Sympcare” is the outcome of our own work, is bonafide and correct to the best of our knowledge and this work has been carried out taking care of Engineering Ethics. The work presented does not infringe any patented work and has not been submitted to any other university or anywhere else for the award of any degree or any professional diploma. 

 Date:                                         




 Shivnandan Verma (0537AL221029)
 Rishiraj Hadge (0537AL221020)
Dinesh Verma (0537AL221012)
Aman Dehariya (0537AL221002)




ACKNOWLEDGEMENT


This project work is the result of guidance and support of various people at SISTec-R without whom all our effort would have been directionless and fruitless. We sincerely thank all of them, for assisting us in completing the dissertation.
              We express our ardent and earnest gratitude to our guide, Dr. Priyanka Bhatele, Department of Computer Science & Engineering, SISTec-R Bhopal and Dr. Priyanka Bhatele, HOD, Department of Computer Science & Engineering-AIML, SISTec-R Bhopal for their help and encouragement at all the stages of our Work. Their guidance and motivation helped us to be fruitful in our effort.
         We also express my heartfelt and profound gratitude to our Director 
Dr. Jyoti Deshmukh for his valuable suggestions and ample resources at all stages of the research work.
Finally, we would like to say that we are indebted to my parents for everything that they have done for us.  All of this would have been impossible without their constant support.  And we also thanks to God for being kind to me and driving me through this journey.










Shivnandan Verma (0537AL221029)
Rishiraj Hadge (0537AL221020)
Dinesh Verma (0537AL221012)
Aman Dehariya (0537AL221002)






Contents
CERTIFICATE	ii
APPROVAL CERTIFICATE	iii
CANDIDATE DECLARATION	iv
ACKNOWLEDGEMENT	v
Chapter 1	3
Introduction	3
1.1 Overview	3
1.2 Problem Statement	3
1.3 Objective (Purpose / Motivation)	3
1.3.2 Encourage Contracting that is open to the public:	4
1.3.3 Ensure Fair Pricing and prompt Payments:	4
1.3.4 Facilitate Market Access for the Farmers:	4
1.3.5 Reduce reliance on Middlemen:	4
1.3.6 Continuous Enhancement of the System:	4
1.4 Applications	4
1.4.1 Access Improvement to the Market:	4
1.4.2 Contract Management:	5
1.4.3 Effective Supply Chain:	5
1.4.4 Financial Security:	5
1.4.5 Empowering Farmers:	5
1.4.6 Economic Effect:	5
1.4.7  Economic sustainability:	6
1.4.8 Productivity through Data Insights:	6
1.4.9 Scalability and Adaptability Features:	6
1.5 summary	6
Requirement Analysis	7
2.1 Team Responsibility Matrix	7
2.2 Gantt chart	8
2.3 Functional Requirements	9
2.4 Non-Functional requirement	11
Chapter 3	14
Designing & Methodology	14
3.1 Overview of Methodology	14
3.1.2	Platform Architecture and Design:	14
3.1.3	User Interface (UI) Design:	14
3.1.4	Integration with Machine Learning (ML):	15
3.2	Feature Development:	15
3.2.1	Contract Management:	15
3.2.2	Price Negotiation:	15
3.2.3	Payment Processing:	15
3.3	Testing & Validation:	15
3.4	Training & Support:	15
3.6	Detailed Methods	16
3.6.1 Understand the Needs:	16
3.6.2	Building the Platform:	16
3.6.3 Key Features Development:	16
3.6.4 Testing and Feedback:	17
3.6.5	Launch and Grow:	17
3.7	Project Modules	17
3.7.1 User Management Module: -	17
3.7.2 Product Listing and Management Module: -	17
3.7.3 Marketplace Module: -	18
3.3.4  Payment Integration Module: -	18
3.8	ARCHITECTURE/BLOCK DIAGRAM	19
3.3.1 User Interfaces (Mobile App in Kotlin):	19
3.3.2 Core Functional Modules:	20
3.4 DIAGRAMS WITH EXPLAINATION	21
3.4.1 FLOW-CHART	21
3.4.2	USE CASE DIAGRAM	23
3.4.3	CLASS DIAGRAM	25
3.4.4	SEQUENCE DIAGRAM	26
3.4.5	DATA FLOW DIAGRAM	27
3.4.6  E-R DIAGRAM	30
Chapter 4	32
4.1	Technology Used	32
4.1.1 Kotlin for Android Development	32
4.1.2	Firebase for Backend Services	32
4.1.3   Screen Shots-	33
4.2	ADVANTAGES	35
4.2.1	Increased Income for Farmers	35
4.2.2 Better Market Access	35
4.2.3 Reduced Dependence on Middlemen	35
4.2.4 Transparency and Fair Transactions	35
4.2.5Improved Efficiency and Convenience	35
4..2.6 Access to Market Trends and Data	35
4.2.7 Empowerment and Financial Inclusion	35
4.2.8Better Resource Management	36
4.2.9Support for Sustainable and Organic Farming	36
4.2.10Local Economy Growth	36
4.2.11 Reduced Food Insecurity	36
Chapter 5	37
5.1 Conclusion	37
5.2 Future Scope	38
5.2.1 Expansion of Market Reach	38
5.2.2 Diversification of Agricultural Products	38
5.2.3	Advanced Technology Integration	38
5.3	References	39
5.3.1	AGRICENTRAL: -	39























 
LIST OF FIGURE

S No	Figure No	Figure Name	Page No
1	Figure 2.2	Gantt Chart 	08
2	Figure 3.1	Block Diagram	18
3	Figure 3.2	Flow Chart 	19
4	Figure 3.3	Use Case Diagram 	21
5	Figure 3.4	Class Diagram	23
7	Figure 3.6	DFD	28

 
LIST OF TABLE

S.No	Table No	Table Name	Page No
1	Table  3.1	  Team Responsibility Matrix	07














 
Chapter 1
Introduction
1.1	Overview

Sympcare addresses major healthcare challenges such as delayed diagnosis, limited access to reliable medical guidance, and rising patient load by providing an AI-driven platform that performs symptom-based disease prediction and delivers personalized health recommendations. Traditional sources of health information are often inconsistent, causing confusion and delayed treatment, but SympCare overcomes these issues through real-time diagnostic support powered by multiple machine learning models. The system guides users from symptom analysis to potential conditions, lifestyle suggestions, and recommended next steps, ensuring faster, more accurate, and accessible preliminary medical assistance. By making early assessment transparent, efficient, and highly accessible, SympCare improves user confidence, enhances healthcare reach, and promotes preventive wellness.

1.2	Problem Statement

In today’s fast-paced environment, individuals often struggle to access timely and reliable health guidance. Many people face difficulties in identifying early symptoms of diseases, understanding skin-related issues, or assessing their mental well-being. Traditional methods—such as visiting clinics for minor symptoms, relying on self-diagnosis, or depending on unverified online information—are often inconvenient, inaccurate, and time-consuming.
These limitations lead to delayed medical attention, increased health risks, and elevated stress levels among individuals who lack immediate support or awareness. Mental health concerns, in particular, often remain unrecognized due to hesitation, lack of guidance, or limited access to professionals. Similarly, early detection of general illnesses and skin diseases becomes challenging without proper tools.
Given these challenges, there is a clear need for an intelligent, accessible, and unified system that can assist users with early disease prediction, skin condition analysis, and mental health assessment. Such a system should provide quick insights, easy interaction, and reliable preliminary guidance, enabling users to make informed decisions about their health before the situation becomes critical.

1.3	Objective (Purpose / Motivation)
for this project the following objectives has been decided.
1.3.1 Provide Early Disease Awareness
Develop a system that allows users to receive instant health insights by analyzing their symptoms. This helps individuals detect possible health issues early and take preventive steps before the condition becomes severe.
1.3.2 Offer Accessible Skin Disease Assessment
Build an automated skin analysis module where users can upload images of their skin conditions. The system will provide awareness by identifying possible skin-related diseases, helping users make informed decisions without delay.
1.3.3 Support Mental Health Evaluation Through Guided Interaction
Create a chatbot-based assessment system that asks personalized questions and evaluates stress, anxiety, or depression levels. This removes hesitation, increases accessibility, and encourages individuals to understand their mental well-being.
1.3.4 Improve User Engagement Through an Interactive Platform
Design a simple and user-friendly interface that allows users to interact effortlessly, regardless of their technical knowledge. This ensures comfortable participation and increases user trust.
1.3.5 Provide a Unified Healthcare Assistance System
Integrate symptom assessment, skin analysis, and mental health evaluation into a single platform. This reduces dependency on scattered information sources and provides users with complete health support at one place.
1.3.6 Ensure Continuous System Enhancement
Develop a system that can be upgraded over time as user needs, health data, and disease patterns evolve. This ensures long-term functionality, accuracy, and relevance of the healthcare assistant.
1.4 Applications
There are several important applications of this project, and some of the major ones are discussed below:
1.4.1 Early Diagnosis Support
The platform helps users identify potential health issues at an early stage by analyzing symptoms, skin conditions, and mental health indicators. This reduces delays in seeking care and encourages timely medical attention, improving overall health outcomes.
1.4.2 Automated Symptom Assessment
The system provides a quick and accessible method for users to understand possible illnesses by entering their symptoms. It reduces reliance on guesswork and unverified sources, offering preliminary guidance that is reliable and easy to interpret.
1.4.3 Skin Disease Analysis
Through automated image-based assessment, users can receive awareness regarding possible skin diseases. This minimizes the need for immediate physical consultation, especially in areas where dermatological services are limited.
1.4.4 Mental Health Screening
The interactive chatbot generates personalized questions and evaluates responses to identify signs of stress, anxiety, or depression. This encourages users to acknowledge their mental health condition and seek support if needed.
1.4.5 User Empowerment Through Health Insights
By providing symptom predictions, skin diagnosis, and mental health evaluations, the platform empowers users to make informed decisions. It improves their understanding of health conditions and guides them toward healthier choices.
1.4.6 Increased Accessibility to Health Guidance
The system provides immediate support without requiring prior medical knowledge, making it beneficial for individuals in remote areas or those hesitant to visit healthcare facilities. This increases the reach of basic health awareness.
1.4.7 Support for Preventive Healthcare
With early alerts and awareness, users can take preventive actions such as lifestyle changes, timely consultations, or early treatment. This contributes to long-term health improvement and reduces medical complications.
1.4.8 Data-Driven Health Insights
The platform can analyze collected data to provide insights into health trends, common symptoms, and frequently occurring mental health patterns. Such data can help improve future recommendations and enhance system performance.
1.4.9 Scalability and Adaptability
The system can be used by individuals across different age groups and regions. Its scalable design allows it to support more users, additional disease categories, and new assessment modules in the future, maintaining long-term relevance.
1.5 summary
In Chapter 1, an effort has been made to address the growing challenges individuals face in accessing timely and reliable health guidance. Many users struggle with early identification of general diseases, skin-related issues, and mental health conditions due to limited awareness, hesitation, or lack of immediate support. To overcome these limitations, a unified and intelligent healthcare prediction platform has been proposed.
This platform integrates three key components—symptom assessment, skin disease analysis, and mental health evaluation—into a single, user-friendly system. It aims to provide early awareness, reliable predictions, and personalized guidance through interactive features such as a chatbot. The system promotes preventive healthcare by offering quick insights that help users make informed decisions before their conditions worsen.
The chapter has also discussed the primary objectives of the system, such as enabling early diagnosis, improving accessibility, empowering users with health insights, and ensuring continuous system enhancement. Additionally, several applications have been highlighted, including support for early prediction, improved accessibility to health information, and the ability to deliver personalized assessments across diverse health domains.
Overall, Chapter 1 establishes the foundation for understanding the need, purpose, and benefits of an AI-powered healthcare prediction system. It sets the stage for further chapters that will explore the system’s detailed architecture, implementation, functionalities, and its potential role in promoting accessible, efficient, and preventive healthcare for a wide range of users.
 
Chapter 2
Requirement Analysis

2.1 Team Responsibility Matrix
Task	Shivnandan
Verma	Dinesh
Verma	Rishiraj
Hadge	Aman
Dehariya
Requirement
Gathering	1	1	1	1
Planning	1	1	1	1
Designing	0	1	0	1
Web Development	1	0	1	1
Documentation	0	1	0	1
Presentation	1	1	1	1

In this matrix, "1" represents Responsible, "0" represents Informed. The roles are defined based on the expertise and contributions of each team member.



2.2 Gantt chart

Weeks	1	2	3	4	5	6	7	8
								
								
Planning								

Design								

Coding								



Figure. 2.1: Gantt Chart










2.3 Functional Requirements


REQUIREMENTS	
DESCRIPTION

USER INTERFACE

FR1	
User Interface	A unified dashboard where users can access all three modules: symptom assessment, skin disease analysis, and mental health evaluation. The interface supports simple navigation, clear instructions, and multilingual accessibility.

FR2	
Symptom Assessment Interface	Allows users to enter symptoms, view predicted diseases, and receive explanation-based insights. Includes fields, dropdowns, and guided symptom selection.

FR3	
Skin Assessment Interface	Provides an upload section for skin images, previews images, and displays predicted skin disease results with confidence scores.

HARDWARE INTERFACE


FR4	Mental Health Chatbot Interface	Enables users to interact with a chatbot that asks personalized questions (1–5 scale), evaluates responses, and provides mental health guidance.

FR5	
Desktop/Laptop	Provides a web-based version for users who prefer larger screens, especially for viewing reports and detailed predictions.

FR6	
Mobile Devices	The system should be accessible on smartphones (Android/iOS), allowing users to conduct assessments anytime for convenience.

FR7	Cloud Infrastructure	All models and user data are hosted on scalable cloud services to ensure high availability, fast processing, and secure data storage.


SOFTWARE INTERFACE


FR10	Machine Learning Models	The system integrates ML/DL models for symptoms, skin detection, and mental health prediction to generate accurate results.

FR11	Mobile/Web Application	The platform should be responsive and operate smoothly on all device types including phones, tablets, and desktops.

FR12	Communication API	Real-time chatbot interaction enables users to answer mental health questions smoothly without delays or miscommunication.

FR13	Image Processing Tools	Integrates preprocessing tools to resize, clean, and normalize skin images before analysis.






2.4 Non-Functional requirement

REQUIREMENTS	
DESCRIPTION

PERFORMANCE REQUIREMENT


NFR1	
Response Time	The platform should respond within 2 seconds for major actions such as symptom submission, image upload processing, and chatbot question transitions.

NFR2	Model Efficiency	ML/DL models should provide predictions within 3–5 seconds to maintain a smooth user experience.

NFR3	
Concurrency	The system should support at least 5,000 concurrent users without performance degradation.

NFR4	
Throughput	Must handle multiple analysis requests per second, especially during peak usage hours.

SAFETY REQUIREMENT

NFR5	
Data Backup	Regular backups of health records, prediction results, and user profiles to prevent data loss.

NFR6	
Disaster Recovery	A defined recovery mechanism ensures the system is restored quickly in case of a major outage.
NFR7	Data Redundancy	User data should be stored in distributed cloud regions to minimize downtime or data loss.

SECURITY REQUIREMENT


NFR8	
User Authentication	Strong authentication (email/OTP or two-factor authentication) ensures secure access for users.

NFR9	
Data Encryption	All sensitive data (symptoms, mental health responses, skin images) must be encrypted during transmission and storage.

NFR10	
Payment Security	Strict user privacy policies must be followed, especially for mental health and skin images.

NFR11	
Vulnerability Management	Routine audits and security checks to identify risks and protect user health data.

SOFTWARE QUALITY ATTRIBUTES

 NFR12	
Maintainability	The system should be modular so components can be updated, fixed, or retrained easily. Clean code and proper documentation must support fast maintenance.

NFR13	
Scalability	The system should handle increasing users, more medical data, and future features without performance issues. It must support vertical and horizontal scaling.

NFR14	
Reliability	The system must provide 99.9% uptime with stable, fault-tolerant architecture. Automatic recovery and backups should ensure continuous service availability.

NFR15	
Usability	The interface should be simple, user-friendly, and suitable even for non-technical users. Clear navigation and multilingual support must improve the user experience.

NFR16	
Efficiency	The system should work smoothly with low memory, CPU, and battery usage. All processes must be optimized for fast performance, especially on mobile devices.


















Chapter 3
Designing & Methodology

3.1 Overview of Methodology
The methodology used to develop the AI-Powered Healthcare Prediction System follows a structured and user-centric approach. It ensures accurate predictions, smooth user experience, and reliable integration of all core modules—symptom assessment, skin disease analysis, and mental health screening. The development process involves key phases such as requirement analysis, system design, model development, integration, testing, and deployment.
The primary aim is to create a unified platform that offers early healthcare insights in a simple, accessible, and efficient manner.
The methodology consists of several phases:
________________________________________
3.1.1 Needs Assessment & User Understanding
•	The first step involves identifying the needs and challenges of users who lack instant access to health guidance.
•	Surveys, interviews, and feedback collection are used to understand user expectations related to symptom checking, skin analysis, and mental health support.
•	Insights from medical students, healthcare professionals, and users help define the essential features of the system.
________________________________________
3.1.2 System Architecture & Design
System Architecture:
A scalable and secure architecture is designed to manage user inputs, analyze disease patterns, process images, and generate predictions. The backend handles text-based symptoms, image uploads, and chatbot responses while maintaining data integrity and performance.
________________________________________
3.1.3 User Interface (UI) Design
A simple and intuitive interface is created to ensure smooth interaction for users of all age groups.
The design includes:
•	Guided forms for symptom entry
•	Image upload interface for skin assessment
•	Chatbot interface for mental health evaluation
The goal is to ensure accessibility even for users with minimal technical experience.
________________________________________
3.1.4 Integration of Machine Learning Components
Machine learning models are integrated into the system to deliver accurate predictions:
•	Classification models for symptom-based disease prediction
•	Image-based deep learning model for skin disease detection
•	A scoring-based mental health model for stress, anxiety, or depression levels
________________________________________
3.2 Feature Development
3.2.1 Symptom Assessment Module
A text-based prediction system where users enter symptoms.
The ML model analyzes these symptoms and predicts possible diseases. Results are displayed in user-friendly formats.
3.2.2 Skin Disease Analysis Module
Users upload images of their skin conditions.
The system preprocesses the images, compares them with trained patterns, and predicts potential skin diseases for awareness.
3.2.3 Mental Health Assessment Module
A chatbot-driven system that asks personalized questions based on the user’s profile.
Responses are analyzed on a scoring scale and mental health conditions (such as stress or depression) are predicted, followed by supportive suggestions.
________________________________________
3.3 Testing & Validation
3.3.1 Multi-Level Testing
The platform undergoes multiple testing stages, including:
•	Functional Testing
•	Usability Testing
•	Accuracy testing for ML predictions
•	Security and performance testing
3.3.2 Pilot Testing
A pilot phase is conducted with selected users to verify real-world performance.
Their feedback is used to improve accuracy, interface usability, and overall functionality.
________________________________________
3.4  Training & Support
3.4.1 User Support System
Continuous support is provided to help users report issues, understand predictions, and interact effectively with the chatbot.
3.4.2 User Guidance
Clear instructions, tooltips, and in-app tutorials ensure that users can easily submit symptoms, upload images, and respond to mental health assessments.
________________________________________
3.5  Deployment & Scaling
3.5.1 Phase-wise Deployment
The platform is initially released to a limited audience for stability monitoring.
Based on feedback and improvements, the system is gradually expanded to a larger user base.
3.5.2 Continuous Monitoring & Updates
Performance, accuracy, and user engagement are regularly analyzed.
Insights are used to update models, enhance features, and introduce new health prediction capabilities.
________________________________________
3.6  Detailed Methods
3.6.1 Understanding User Needs
Interviews, surveys, and real-life observation are used to identify how users describe symptoms, what skin issues they face, and what mental health guidance they expect.
3.6.2 System Development
A secure backend is built to handle text, images, and chatbot conversations.
Machine learning models are trained on reliable datasets to ensure accurate predictions.
The interface is kept simple to support users with varying levels of digital literacy.
3.6.3 Feature Implementation
•	Disease Prediction: Users enter symptoms to receive possible disease outcomes.
•	Skin Analysis: Users upload images to get skin disease predictions.
•	Mental Health Evaluation: A chatbot asks guided questions and predicts mental health conditions based on responses.
3.6.4 Testing & Feedback Collection
A small user group tests the system.
Issues, errors, and unclear UI areas are corrected based on feedback.
3.6.5 Launch & Growth
After successful testing, the system is launched on a wider scale.
Feedback is continuously collected to improve accuracy, interface quality, and reliability over time.
________________________________________
3.7 Project Modules
3.7.1 User Management Module
•	User registration and login
•	Profile management (age, gender, habits, medical background)
•	Role management (User/Admin)
•	Multi-language support
•	Secure access and data handling
________________________________________
3.7.2 Symptom Input & Disease Prediction Module
•	Users enter symptoms
•	Backend processes and maps symptoms
•	ML-based disease prediction
•	Clear, understandable result display
________________________________________
3.7.3 Skin Disease Analysis Module
•	Image upload and preprocessing
•	Skin disease classification
•	Display of possible conditions and next-step recommendations
________________________________________
3.7.4 Mental Health Assessment Module
•	Chatbot conversation handling
•	Personalized question generation
•	Likert-scale response collection
•	Prediction of stress, anxiety, or depression
•	Automated suggestions for well-being
________________________________________
3.7.5 Communication & Engagement Module
•	Chatbot for mental health guidance
•	Auto-suggestions and tips
•	Follow-up question handling
________________________________________
3.7.6 Localization & Accessibility Module
•	Multi-language support
•	Region-based UI adjustments
•	Voice-assisted interaction (optional future enhancement)

3.4 DIAGRAMS WITH EXPLAINATION

3.4.1 FLOW-CHART


 
Figure 3.2: Flow-Chart


1. User Authentication
•	Register:
If the user (patient or doctor) does not have an account, they can register by filling in basic details.
•	Login:
Existing users authenticate and proceed into the system.
________________________________________
2. Dashboard (Role-Based Access)
Successful login ke baad user ko unke role ke hisaab se dashboard milta hai:
________________________________________
A. Patient Dashboard
Patient multiple health-related features access kar sakta hai:
a) Symptom Assessment
•	User symptoms enter karta hai
•	AI model disease prediction generate karta hai
b) Book Appointment
•	Doctor list browse
•	Time slot select
•	Appointment confirm
c) Doctor Consultation
•	Video/audio/physical consultation
•	Doctor notes + prescriptions
d) Medication Reminders
•	System medicines ke time pe notifications deta hai
e) Mental Health Support
•	Stress assessment
•	Basic mental health guidance
•	Emergency help prompts
f) Health Education
•	Blogs, videos, articles, tips
•	Disease awareness content
g) Profile Management
•	Personal/medical history update
•	Uploaded reports
•	Past appointments
________________________________________
B. Doctor Dashboard
Doctor apne operations manage kar sakte hain:
a) Access Patient Information
•	Patient history
•	Symptoms
•	Reports
•	Previous visits
b) Manage Appointments
•	Approve/reject bookings
•	Reschedule
•	Daily schedule view
c) Provide Health Advice
•	Diagnosis
•	Prescription
•	Follow-up notes
•	Lifestyle recommendations
d) Report Generation
•	Patient records summary
•	Visit history
•	Treatment notes
________________________________________
C. Admin Dashboard
Admin pura system control karta hai:
a) Manage Users
•	Add/delete/update patient & doctor accounts
b) Oversee System Operations
•	Appointment tracking
•	System logs
•	Monitoring performance
c) Real-Time Queuing & Updates
•	Doctor queues
•	Appointment waiting time
•	Real-time alerts
d) Reports & Analytics
•	User activity
•	Health trends
•	Hospital metrics

3. Return to Homepage
•	Dashboard
•	Home Page
•	Previous Screens

3.4.2	USE CASE DIAGRAM
This system flowchart demonstrates the roles, interactions, and functionalities of a digital platform aimed at connecting farmers and buyers. It highlights a structured approach to managing key tasks such as product listings, price negotiations, and transactions, with administrative oversight to ensure fair and efficient operations.
 
Figure 3.3 Use case 


This use case describes how different users (Patient, Doctor, and Admin) interact with the healthcare application and how the system responds to their actions.
1. Start
The process begins when a user opens the healthcare application (web or mobile).
2. User Authentication
The system checks whether the user has an account.
• Register
If the user is new, they create an account by entering required personal and medical details.
• Login
Existing users log in to access their respective dashboards.
Users are categorized into:
•	Patient
•	Doctor
•	Admin

3. Use Cases Based on User Roles
A. Patient Use Cases
1. Symptom Assessment
•	Patient enters symptoms.
•	The system analyses symptoms and provides AI-based health predictions.
2. Book Appointment
•	Patient views the list of doctors.
•	Selects a date/time.
•	Confirms appointment.
3. Doctor Consultation
•	Can attend online or in-person consultation.
•	Receives diagnosis, prescription, and follow-up instructions.
4. Medication Reminders
•	System sends timely medicine alerts.
•	Patient receives notifications.
5. Mental Health Support
•	Patient can use self-assessment tools.
•	Receives mental health tips and support content.
6. Health Education
•	Patient accesses curated articles, videos, and health tips.
7. Profile Management
•	View/update personal information.
•	View medical history, past appointments, and prescriptions.
________________________________________
B. Doctor Use Cases
1. Access Patient Information
•	Doctor views patient records, symptoms, reports, and history.
2. Manage Appointments
•	Approve, cancel, or reschedule patient bookings.
3. Provide Health Advice
•	Provide diagnosis.
•	Upload prescriptions.
•	Give lifestyle recommendations.
4. Generate Reports
•	Generate medical summaries for patients.
•	Access past consultation notes.
________________________________________
C. Admin Use Cases
1. Manage User Accounts
•	Add, update, or remove Patients and Doctors.
2. Oversee System Operations
•	Track activity logs.
•	Monitor system performance.
3. Real-Time Queue & Updates
•	Manage doctor queues.
•	Monitor appointment status.
4. Generate System Reports
•	View analytics such as:
o	User activity
o	Appointment trends
o	System usage statistics
.



3.4.3	CLASS DIAGRAM

   

Figure 3.4:  Class Diagram
This diagram is a Class Diagram that represents the structure and interactions within an AI-powered healthcare management and prediction system. It defines the core entities—Patient, Doctor, Admin, Profile, Symptom Prediction Model, Skin Disease CNN Model, Mental Health MLP Model, and Chatbot System—along with their attributes and methods. The diagram illustrates how these entities collaborate to enable symptom prediction, doctor consultation, mental health support, system management, and AI-driven healthcare assistance.
Each class has clearly defined responsibilities:
1.Patient
The Patient class stores personal information such as name, age, gender, symptoms, and uploaded medical images.
Patients interact with the system to assess symptoms, receive predictions, manage profiles, and communicate with doctors.
2. Profile
The Profile class maintains the patient's medical history, reports, and appointment records.
It acts as a central repository for all patient-related data that doctors and AI models may use for decision-making.
3. Doctor
The Doctor class contains attributes like name, specialization, and feedback.
Doctors access patient information, provide diagnoses, share prescriptions, and manage appointments.
4. Admin
The Admin class handles high-level system management, including user account control and monitoring application operations.
Admins ensure smooth functioning and integrity of the healthcare platform.
5. Symptom Prediction Model
This AI model analyzes text-based symptoms provided by the patient.
Its primary function is to predict potential diseases, enabling early guidance even before doctor consultation.
6. Skin Disease CNN Model
This model processes uploaded skin images to detect possible skin diseases.
It uses image classification to deliver accurate and fast predictions.
7. Mental Health MLP Model
This model evaluates patient responses to mental health questionnaires.
It predicts mental well-being levels and flags the need for psychological support.
8. Chatbot System
The Chatbot class is responsible for generating AI-driven questions and providing health guidance.
It supports patients through automated conversation, educational tips, and mental health suggestions.
Overall Interaction
The class diagram demonstrates how patients provide inputs (symptoms, images, or responses), which are processed by different AI models, and how doctors use these insights to deliver accurate diagnoses.
Admins manage the system, while the chatbot enhances patient engagement through automated assistance.

3.4.4	DATA FLOW DIAGRAM
DFD – Level 0 (Context Diagram)
This top-level diagram shows the entire system as a single process (AI-Powered Healthcare Assistant System) and how external entities interact with it.
External Entities
•	User (Patient)
•	Doctor / Healthcare Provider
•	Authentication Service
•	Database System
Level 0 Data Flows
•	User → Login/Registration Data → System
•	System → Dashboard, Health Reports, Recommendations → User
•	User → Symptoms, Chats, Appointments → System
•	System → Medical Advice, Appointment Updates → User
•	System ↔ Database → User Profiles, Reports, Chat History
DFD – Level 1 (Detailed Process Breakdown)
This level expands the main system into multiple processes.
Processes
1.	User Authentication
2.	Dashboard Management
3.	Symptom Checker (AI Model)
4.	Chat Module (AI + Live Doctor)
5.	Profile Management
6.	Appointments Module
7.	Health Records & Reports Module
________________________________________
Process 1: User Authentication
Data In: Registration Data / Login Credentials
Data Out: Authenticated User Token
Data Stores Used: User Database
External Entity: Authentication Service
Flow:
User → Credentials → Authentication → User Verified → Dashboard Access
________________________________________
Process 2: Dashboard Management
Data In: User ID
Data Out: Quick Stats, Suggested Checks, Reports Preview
Data Stores: User Database, Reports Database
________________________________________
Process 3: Symptom Checker (AI Model)
Data In: Symptoms List
Processes:
•	Preprocessing
•	Prediction by ML Model
•	Risk Score Generation
Data Out: Possible Diseases, Recommendations
Data Store: AI Model Knowledge Base
________________________________________
 
1.	Figure : DFD

Process 4: Chat Module
Inputs: User Query
Processes:
•	Chat with AI (NLP Model)
•	Optional: Chat with Doctor
Outputs: Medical Advice / Follow-Up Suggestions
Data Stores: Chat History
Process 5: Profile Management
Data: User personal details, health preferences
Stores: User Database
Out: Updated Profile
Process 6: Appointments Module
Data In: Appointment Request
Processes:
•	Slot Checking
•	Booking / Cancellation
Data Out: Appointment Confirmation
Stores: Appointment Database
Process 7: Health Records & Reports
Data In: Uploaded Reports / Generated Reports
Processes:
•	Storage
•	Retrieval
•	Visualization
Data Out: Report View, Downloadable PDF
Stores: Reports Database







Chapter 4
Implementation and Results Analysis


4.1	Technology Used
4.1.1 Kotlin for Android Development
Kotlin a statically-typed programming language developed by JetBrains, is designed to be fully interoperable with Java and has become the official language for Android app development. Kotlin's concise syntax, null safety, and compatibility with Android make it an ideal choice for this app, providing a clean and user-friendly interface for farmers and consumers alike.
4.1.2	Firebase for Backend Services
Firebase, a Google-backed platform, offers a suite of tools for building and managing mobile applications, including real-time database, authentication, cloud storage, and machine learning capabilities. Using Firebase, this app supports:
o	Real-time Database: For storing and syncing data in real-time, providing instant updates on marketplace listings, comments, and crop health diagnostics.
o	Firebase Authentication: Allowing secure sign-in options, including Google sign-in, to simplify user on boarding.
o	Firebase Cloud Storage: For storing images and videos of produce and crop health images.




4.1.3   Screen Shots-

 


                     HOME PAGE



  

Log in                                         Register

Develop a mobile app that connects farmers directly with consumers and retailers, featuring produce listings, price negotiation, and secure transaction management, empowering farmers to earn fair prices by eliminating intermediaries.  
4.2	ADVANTAGES
4.2.1	Increased Income for Farmers
•	Farmers can directly sell their produce to consumers and retailers, eliminating middlemen. This results in higher profits by retaining a larger share of the sale price.
4.2.2 Better Market Access
•	The app expands the farmer's reach, allowing them to connect with a broader range of consumers, including urban and international buyers. This increases sales opportunities beyond local markets.
4.2.3 Reduced Dependence on Middlemen
•	By removing intermediaries, farmers can negotiate directly with buyers, keeping prices fair and transparent. This allows farmers to control their pricing and increase their profit margins.
4.2.4 Transparency and Fair Transactions
•	The app provides clear pricing, secure payment processing, and transparent agreements between farmers and buyers. This ensures fair dealings with fewer disputes and delays.
4.2.5Improved Efficiency and Convenience
•	Farmers can easily list, update, and manage their produce on the platform, providing real-time availability information. This streamlines the order and delivery process for both farmers and buyers.
4..2.6 Access to Market Trends and Data
•	Farmers receive valuable insights into market demand, price trends, and consumer preferences. This helps them plan crops, adjust pricing, and optimize production for better sales outcomes.
4.2.7 Empowerment and Financial Inclusion
•	Small and rural farmers gain access to wider markets, leveling the playing field. Digital payment systems also offer them financial services and greater access to capital.
4.2.8Better Resource Management
•	Direct sales help farmers manage inventory more effectively and reduce waste. With real-time data, they can adjust production based on demand, improving cost efficiency.
4.2.9Support for Sustainable and Organic Farming
•	Farmers using sustainable or organic practices can showcase their eco-friendly products, attracting environmentally conscious consumers. The app fosters awareness of sustainable agriculture.
4.2.10Local Economy Growth
•	Direct sales to consumers and retailers help retain more economic value within local communities. This boosts local economies and provides more opportunities for small businesses to thrive.
4.2.11 Reduced Food Insecurity
•	Consumers gain reliable access to fresh, locally grown produce, improving food security in urban areas. The app creates shorter, more resilient supply chains for fresh food delivery.










	Chapter 5	
Conclusion & Future Scope

5.1 Conclusion
The proposed AI-Powered Healthcare Prediction System is an innovative solution aimed at providing accessible and early health insights to users. By integrating general disease prediction, skin disease analysis, and mental health assessment, the system offers a comprehensive platform for preventive healthcare. This digital approach empowers users to take proactive steps toward their well-being, improving awareness and accessibility in healthcare.
5.1.1 Comprehensive Health Support
•	General Disease Prediction: Users can input their symptoms and receive predictions about possible diseases, helping in early diagnosis.
•	Skin Disease Detection: By uploading images of skin conditions, users can get awareness about potential skin-related issues.
•	Mental Health Assessment: Personalized chatbot interactions help predict conditions like stress, depression, or anxiety and provide supportive suggestions.
5.1.2 User Engagement and Accessibility
•	Interactive Interface: The chatbot interface ensures an engaging and user-friendly experience.
•	Ease of Use: Even users with minimal digital literacy can access the system effectively.
•	Awareness and Preventive Care: Provides real-time insights and suggestions, enabling users to take preventive measures.
5.1.3 Technological Integration
•	AI & Machine Learning Models: Integration of multiple models improves prediction accuracy for diseases and mental health conditions.
•	End-to-End System: Combines text-based symptom analysis, image processing for skin conditions, and mental health evaluation in a unified platform.
________________________________________
5.2 Future Scope
5.2.1 Expansion of Healthcare Modules
•	Additional Disease Coverage: Expand the system to include more disease categories and rare conditions.
•	Advanced Mental Health Metrics: Incorporate more comprehensive psychological assessments.
•	Personalized Recommendations: Provide diet, exercise, and lifestyle suggestions based on user profiles.
5.2.2 Technological Advancements
•	AI Enhancements: Use advanced deep learning models for improved accuracy in image-based and symptom-based predictions.
•	Mobile App Integration: Develop mobile applications to increase accessibility and reach.
•	Wearable Device Integration: Integrate with health wearables to provide real-time monitoring and predictive alerts.
5.2.3 User Engagement and Data Analytics
•	Personalized Insights: Provide users with tailored health reports and trend analysis.
•	Predictive Analytics: Forecast health risks and suggest preventive measures using data-driven insights.
•	Telemedicine Integration: Collaborate with healthcare providers for consultations based on system predictions.
________________________________________
5.3 References
1.	Healthcare AI Systems: Various research papers and case studies on AI-based disease prediction systems.
2.	Deep Learning for Medical Imaging: Studies demonstrating convolutional neural networks (CNNs) for skin disease classification.
3.	Mental Health Chatbots: Research on chatbot-based mental health assessments and digital interventions.
4.	Machine Learning in Preventive Healthcare: Literature on symptom analysis, predictive analytics, and healthcare decision support systems.














































