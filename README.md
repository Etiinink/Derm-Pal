# Derm-Pal
DermPal: AI-Powered Personalized Acne & Skin Type Diagnosis
🌟 Project Overview
DermPal is an innovative AI-powered web application designed to democratize access to preliminary dermatological diagnosis. It uniquely combines skin-type classification with precise acne diagnosis, providing users with personalized skincare recommendations and addressing the critical shortage of dermatologists, especially in underserved regions like Nigeria.

💡 Problem Statement
Acne is a pervasive global concern, affecting approximately 85% of teenagers and young adults. Beyond its physical manifestations like scarring and hyperpigmentation, acne significantly impacts mental health, leading to issues such as depression and low self-esteem.

A critical challenge is that acne presents differently across various skin types (oily, dry, normal, combination), yet many existing AI diagnostic tools overlook this crucial distinction, hindering personalized treatment. Furthermore, access to dermatological care is severely limited in many parts of the world, particularly in Africa. In Nigeria, for instance, fewer than 200 practicing dermatologists serve a population exceeding 200 million, creating an alarming patient-to-specialist ratio and leading to delayed diagnoses and treatments.

✨ Solution & Innovation
DermPal offers an accessible, web-based solution that leverages Convolutional Neural Networks (CNNs) to analyze facial images. It performs a dual classification: identifying the user's skin type (dry, oily, normal) and diagnosing specific acne forms (comedones, nodular/cystic, papules/pustules). Based on this comprehensive diagnosis, DermPal provides personalized skincare recommendations, guiding users in managing their routine and selecting appropriate over-the-counter products.

Key Innovative Aspects:
Holistic and Personalized Diagnosis:

DermPal's primary innovation is its dual-classification approach, simultaneously identifying skin types and acne forms. This goes beyond generic acne diagnosis, providing a foundational understanding of the user's unique skin context.

This integrated classification is paramount because skin type profoundly influences acne manifestation and treatment efficacy. By providing both, DermPal enables the generation of personalized skincare recommendations, a feature largely absent or rudimentary in current AI diagnostic tools, empowering users to make informed choices.

Addressing a Critical Healthcare Gap with Accessibility:

DermPal directly tackles the global shortage and uneven distribution of dermatologists, particularly in underserved regions. By offering an accessible, web-based AI solution, we democratize early diagnosis and guidance, reducing the burden on overstretched healthcare systems and minimizing diagnostic delays.

The web-based nature ensures broad reach, making professional-grade preliminary skin assessment available to anyone with internet access, regardless of their geographical location or socioeconomic status.

Advanced AI Application for Generalization:

Leveraging Convolutional Neural Networks (CNNs) with TensorFlow and Keras for image analysis is a robust technical choice. Our innovative application of transfer learning algorithms was crucial in overcoming challenges related to model generalization, ensuring high accuracy and reliability across diverse user images. This iterative refinement of the AI model demonstrates a sophisticated approach to achieving robust performance in a complex diagnostic domain.

Ethical and Diverse Data Sourcing:

Our commitment to ethical data collection, including primary data sourcing from willing Covenant University students with explicit consent and CHREC authorization (approval number CHREC /405/2023), is an innovative step towards building more representative and reliable datasets. This primary data, combined with diverse secondary sources from Kaggle, contributes to a more robust and generalizable AI model, essential for accurate skin type and acne classification across various demographics.

🛠️ Technology Used
Frontend: HTML, CSS, JavaScript

Backend Framework: Flask

Machine Learning: TensorFlow, Keras, Convolutional Neural Networks (CNNs), Transfer Learning

Deployment: (Currently focused on local deployment; future plans for cloud platforms like GCP/AWS/Azure)

📊 Data Used
The project utilized a combination of primary and secondary facial image data for training the skin type and acne classification models.

Primary Sourcing: 15 images were ethically sourced from willing Covenant University students with explicit consent and authorization from the Covenant Health Research Ethics Committee (CHREC /405/2023). These images were captured using mobile devices and sorted into classes for dry, oily, and normal skin types, and comedones, cystic, and pustular acne.

Secondary Sourcing: Additional facial images were obtained from Kaggle, an online data science platform.

Acne Dataset (YOLOv8 Format with Roboflow Labelling): 927 images

Acne Dataset from Kaggle: 1800 images (final dataset for training after sorting unusable images)

Skintype by Dissanayake Shakya: 3125 images (entire dataset used for skin type classifier)

🎯 Target Audience & Impact
Target Audience:

Teenagers and young adults (12-30 years old) globally, particularly in regions with limited access to dermatological care (e.g., Nigeria).

Parents, guardians, and general healthcare practitioners seeking preliminary skin health assessments.

Impact:

Improved Mental Health: Provides accessible, timely diagnoses, empowering users and mitigating the psychological burden of acne.

Democratized Healthcare Access: Bridges the gap in dermatological care, especially in underserved areas, reducing diagnostic delays.

Reduced Healthcare Burden: Lessens the load on scarce dermatological professionals by handling preliminary diagnoses.

Informed Skincare: Empowers users with personalized recommendations for effective self-management and product selection.

Potential for Public Health Insights: Anonymized data could inform future public health initiatives.

🚧 Challenges Encountered
Developing DermPal presented several hurdles, which were instrumental in refining our approach:

Data Quality: Acquiring high-quality, diverse datasets for both acne and skin-type classification proved challenging.

Internet Access: As a web-based application, ensuring accessibility for users in remote areas with poor or no internet connectivity remains a consideration for future development.

Model Performance: Initial CNN models struggled with generalization. This was effectively addressed through the strategic application of transfer learning algorithms, significantly improving accuracy and robustness.

Model Hosting: The weight of the trained models made it difficult to host the web application on free hosting platforms, highlighting the need for dedicated cloud infrastructure in future scaling.

🏆 Competition Achievement
DermPal proudly emerged as one of the top ten (10) finalists in the RAIN Hackathon 1.0, out of over 300 entries. This achievement validates the project's innovative potential and its relevance in addressing critical healthcare challenges.

🚀 Implementation Plan & Scalability (Future Roadmap)
Our vision for DermPal extends beyond the hackathon, with a multi-phase plan for growth and impact:

Phase 1: Model Refinement & Clinical Validation: Further expand diverse data collection, optimize AI models with continuous user feedback, and seek preliminary clinical review for validation.

Phase 2: Feature Expansion & UX Enhancement: Implement user accounts for progress tracking, integrate comprehensive educational content, explore pilot teledermatology integrations, and develop native mobile applications.

Phase 3: Scalability & Outreach: Migrate to robust cloud infrastructure (e.g., GCP, AWS) for elastic scalability, forge strategic partnerships with healthcare organizations, implement multi-language support, and explore sustainable monetization models.

💻 How to Run Locally (For Developers)
To set up DermPal on your local machine:

Clone the repository:

git clone https://github.com/your-username/DermPal.git
cd DermPal

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

(Note: requirements.txt should contain Flask, TensorFlow, Keras, Pillow, etc.)

Place your trained models:

Ensure your trained CNN models (e.g., .h5 or SavedModel format) for skin type and acne classification are placed in the appropriate directory (e.g., models/).

Run the Flask application:

python app.py

Access the application:
Open your web browser and navigate to http://127.0.0.1:5000/.

🤝 Contributing
We welcome contributions to DermPal! If you have suggestions, bug reports, or want to contribute code, please feel free to open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
For any inquiries or collaborations, please reach out to:
Emmanuella Nkanang
nkanangetiini@gmail.com 
