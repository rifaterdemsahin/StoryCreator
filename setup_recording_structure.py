import os

base_dir = "recordings"
versions = ["original_script", "rewritten_script"]

structure = {
    "01_course_intro": {},
    "02_module_1_attackers_playbook": {
        "01_evasion_attacks": {},
        "02_data_poisoning": {},
        "03_model_extraction": {}
    },
    "03_module_2_building_the_shield": {
        "01_adversarial_training": {},
        "02_input_sanitization": {},
        "03_differential_privacy": {}
    },
    "04_module_3_security_lifecycle": {
        "01_red_team_methodology": {},
        "02_security_metrics": {},
        "03_complete_security_lifecycle": {}
    },
    "05_outro_promo": {
        "01_outro": {},
        "02_promo": {}
    }
}

def create_structure(current_path, structure_dict, version_name=None):
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    
    # Create README.md
    readme_path = os.path.join(current_path, "README.md")
    folder_name = os.path.basename(current_path)
    
    title = folder_name.replace("_", " ").title()
    content = f"# {title}\n\n"
    
    if version_name:
        content += f"**Version:** {version_name.replace('_', ' ').title()}\n\n"
        
    if not structure_dict:
        content += "Place your video/audio recording files for this section here.\n"
    else:
        content += "This directory contains subfolders for the individual videos in this section.\n"
        
    with open(readme_path, "w") as f:
        f.write(content)

    # Recurse
    for key, value in structure_dict.items():
        create_structure(os.path.join(current_path, key), value, version_name)

# Create root
if not os.path.exists(base_dir):
    os.makedirs(base_dir)
with open(os.path.join(base_dir, "README.md"), "w") as f:
    f.write("# Course Recordings\n\nThis folder contains the directory structure for recording the course videos.\n\nIt is split into two main versions:\n1. **Original Script**\n2. **Rewritten Script**\n")

# Create versions
for version in versions:
    version_path = os.path.join(base_dir, version)
    create_structure(version_path, structure, version)

print(f"Directory structure created in {os.path.abspath(base_dir)}")
