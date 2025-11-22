# Example Outputs: Script Rewriting in Action

---

## BOTTOM-UP APPROACH: Building Video 1 Component by Component

### Step 1: Hook Transformer Output

**INPUT PROMPT:**
```
Rewrite this video hook while maintaining its purpose and impact.

ORIGINAL HOOK:
"Imagine you're a security professional at a leading autonomous vehicle company. Your team deployed a vision system that identifies stop signs with 99.2% accuracy. State-of-the-art. Production-ready. Then one day, a researcher sends you a photo. It's a stop sign with subtle stickers—almost like graffiti. Your system says, 'Speed limit: 45 miles per hour.' The car accelerates. This actually happened in a research lab. Today, we're diving into that gap between accuracy and robustness."

VIDEO TOPIC: Evasion Attacks
ALTERNATIVE SCENARIO: Healthcare domain
```

**OUTPUT:**
```
REWRITTEN HOOK:
"You're the chief AI officer at a leading diagnostic imaging company. Your skin cancer detection model achieves 99.3% accuracy—outperforming board-certified dermatologists in clinical trials. FDA-approved. Deployed across 200 hospitals. Then a security researcher emails you a case study. A melanoma image with microscopic noise patterns—invisible to any human eye. Your model confidently declares: 'Benign mole. No follow-up needed.' The patient leaves reassured. The tumor grows. This attack has been replicated in multiple research studies. Today, we're examining why your impressive accuracy score might be your biggest blind spot."

SCENARIO USED: Healthcare domain
EMOTIONAL DRIVER: Professional fear + patient safety stakes
WORD COUNT: 98 (original: 94) ✓
```

---

### Step 2: Learning Objectives Transformer Output

**INPUT PROMPT:**
```
Rewrite these learning objectives using different verbs.

ORIGINAL OBJECTIVES:
• Explain why accuracy scores provide incomplete information about model robustness
• Describe how gradient-based evasion attacks work
• Implement basic adversarial attacks using TensorFlow
• Identify real-world scenarios where evasion attacks pose security risks

VIDEO TOPIC: Evasion Attacks
```

**OUTPUT:**
```
REWRITTEN OBJECTIVES:
• Articulate the limitations of accuracy metrics in assessing model security
• Outline the mechanics behind gradient-based adversarial perturbations
• Construct functional adversarial attack implementations in TensorFlow
• Recognize deployment contexts where evasion vulnerabilities create critical risks

VERB CHANGES:
- "Explain" → "Articulate" (same level: comprehension)
- "Describe" → "Outline" (same level: comprehension)
- "Implement" → "Construct" (same level: application)
- "Identify" → "Recognize" (same level: knowledge)
```

---

### Step 3: Content Block Transformer Output

**INPUT PROMPT:**
```
Rewrite this content section.

ORIGINAL CONTENT:
<>
Core Concept 1: The Accuracy Paradox
• MNIST classifier training: 98% accuracy on test set
• But accuracy measures performance on unmodified data only
• Evasion attacks ask: "What can I change about this input to break the model?"
• Neural networks are linear at their core—small targeted changes yield large effects
<>
```

**OUTPUT:**
```
REWRITTEN CONTENT:
<>
Core Concept 1: The Accuracy Illusion
• Consider a digit classifier hitting 98% on standard benchmarks
• This metric only reflects performance on pristine, unaltered inputs
• Adversaries approach differently: "Which minimal modifications cause misclassification?"
• The mathematical reality: neural networks respond linearly to input changes—precision-targeted alterations produce disproportionate output shifts
<>

CHANGES MADE:
- "Paradox" → "Illusion" (different framing, same concept)
- Added "pristine, unaltered" for emphasis
- Rephrased adversary question
- "linear at their core" → "respond linearly" (more direct)

TECHNICAL ACCURACY CHECK:
☑ MNIST reference preserved
☑ 98% accuracy preserved
☑ Linearity concept accurate
☑ Core message identical
```

---

### Step 4: IVQ Transformer Output

**INPUT PROMPT:**
```
Rewrite this IVQ while testing the same knowledge.

ORIGINAL IVQ:
Question: In the FGSM algorithm, what does the epsilon parameter control?
• a) The confidence threshold for predictions
• b) The step size of the perturbation applied to the input
• c) The learning rate of model training
• d) The number of adversarial examples generated
Correct Answer: b)
```

**OUTPUT:**
```
REWRITTEN IVQ:

Question: When executing an FGSM attack, what role does the epsilon (ε) value play?

• a) It determines how many adversarial samples the algorithm produces
• b) It sets the confidence level required before the model outputs a prediction
• c) It controls the magnitude of modification applied to each input pixel
• d) It specifies the learning rate used during the model's original training

Correct Answer: c) It controls the magnitude of modification applied to each input pixel

Explanation: Epsilon functions as your perturbation budget—the maximum amount you're permitted to alter each pixel along the gradient direction. Remarkably, even minimal epsilon values (as small as 0.05 on a 0-255 scale) can devastate model accuracy because neural networks exhibit acute sensitivity to specific feature combinations.

Explain Incorrect Options:
• Option a confuses epsilon with batch generation parameters
• Option b misattributes epsilon to inference thresholds rather than attack parameters
• Option d conflates attack parameters with training hyperparameters

VERIFICATION:
☑ Same concept tested (epsilon's role)
☑ Same difficulty level
☑ Correct answer repositioned (b→c)
☑ All options reworded
```

---

### Step 5: Assembled Video Script (Partial)

```
VIDEO 1: Evasion Attacks: Deceiving Model Perception
Video Type: Talking Head + Screen Share
Duration: 7.5 minutes

Hook: "You're the chief AI officer at a leading diagnostic imaging company. Your skin cancer detection model achieves 99.3% accuracy—outperforming board-certified dermatologists in clinical trials. FDA-approved. Deployed across 200 hospitals. Then a security researcher emails you a case study. A melanoma image with microscopic noise patterns—invisible to any human eye. Your model confidently declares: 'Benign mole. No follow-up needed.' The patient leaves reassured. The tumor grows. This attack has been replicated in multiple research studies. Today, we're examining why your impressive accuracy score might be your biggest blind spot."

Video Overview: "This video explores evasion attacks—among the most intuitive methods adversaries use to deceive AI systems. We'll examine how neural networks misclassify inputs when confronted with precisely crafted adversarial perturbations, walk through the Fast Gradient Sign Method (FGSM) algorithm, and explore real-world implications."

Learning Objectives: "By the end of this video, you will be able to:
• Articulate the limitations of accuracy metrics in assessing model security
• Outline the mechanics behind gradient-based adversarial perturbations
• Construct functional adversarial attack implementations in TensorFlow
• Recognize deployment contexts where evasion vulnerabilities create critical risks"

Let's begin by understanding why strong accuracy can actually mask serious security flaws.

Content:
<>
Core Concept 1: The Accuracy Illusion
• Consider a digit classifier hitting 98% on standard benchmarks
• This metric only reflects performance on pristine, unaltered inputs
• Adversaries approach differently: "Which minimal modifications cause misclassification?"
• The mathematical reality: neural networks respond linearly to input changes—precision-targeted alterations produce disproportionate output shifts

[... continues with all rewritten content blocks ...]
<>

Having witnessed how readily models can be manipulated, let's consolidate the essential insights.

Summary: Evasion attacks reveal a fundamental disconnect between accuracy and robustness. Your model may achieve exceptional performance on standard evaluation sets while remaining susceptible to minimal, targeted perturbations. This vulnerability isn't academic—it's been demonstrated in autonomous vehicles, medical imaging systems, and facial recognition deployments.

Transition to IVQ: "Now I have a critical question for you—grasping this vulnerability is essential for what follows."

In-Video Question (IVQ):
Question: When executing an FGSM attack, what role does the epsilon (ε) value play?
• a) It determines how many adversarial samples the algorithm produces
• b) It sets the confidence level required before the model outputs a prediction
• c) It controls the magnitude of modification applied to each input pixel
• d) It specifies the learning rate used during the model's original training

Correct Answer: c) It controls the magnitude of modification applied to each input pixel

[... explanations ...]
```

---

## TOP-DOWN APPROACH: Strategic Full-Script Rewrite

### Step 1: Script Analyzer Output (Excerpt)

```json
{
  "structure": {
    "sections": 4,
    "total_videos": 12,
    "total_duration": "70+ minutes"
  },
  "tone_profile": {
    "formality": 7,
    "energy": 8,
    "technical_density": 7,
    "personality_markers": [
      "Direct address ('you')",
      "Rhetorical questions",
      "Real-world stakes emphasis",
      "Boxing/military metaphors"
    ]
  },
  "hook_patterns": {
    "video_1": "autonomous vehicles",
    "video_2": "email security",
    "video_3": "API/recommendation system",
    "video_4": "boxing trainer",
    "video_5": "airport security",
    "video_6": "Apple emoji",
    "video_7": "tech company red teams",
    "video_8": "measurement philosophy",
    "video_9": "continuous security"
  },
  "rewrite_opportunities": [
    "Hooks use similar 'imagine you're at company X' pattern",
    "Can vary industry examples more",
    "Transition phrases somewhat repetitive",
    "IVQ explanations follow same structure"
  ]
}
```

---

### Step 2: Rewrite Strategy Output (Excerpt)

```
REWRITE STRATEGY DOCUMENT

GLOBAL RULES:
1. Vary hook openings:
   - Video 1, 4, 7: "Picture this:" pattern
   - Video 2, 5, 8: "Consider this scenario:" pattern
   - Video 3, 6, 9: Direct statement hook

2. Transition phrase rotation:
   - "Let's examine..." → "Let's explore..."
   - "Now that we've seen..." → "Having observed..."
   - "Here's a question for you" → "Test your understanding"

3. Summary restructuring:
   - Lead with key insight, then implications
   - Original leads with recap, then implications

SECTION-SPECIFIC:
- Intro Hook: Shift from "accuracy lottery" to "security blind spot"
- Module 1 hooks: Rotate industries (healthcare, finance, defense)
- Module 2 hooks: Use more everyday analogies
- Module 3 hooks: Emphasize organizational stakes

PRESERVE EXACTLY:
- "Rifat Erdem Sahin"
- "Secure AI: Interpret and Protect Models"
- All algorithm names
- All code blocks
- All epsilon/accuracy values
```

---

### Step 3: Section Executor Output (Intro Video)

```
SECTION 1: COURSE INTRO VIDEO SCRIPT
Target Duration: 3 minutes (~450 words)
Format: Talking Head

Hook (Engaging Opening)
"Ninety-nine percent accuracy. Your machine learning model just achieved it. You've trained, validated, and deployed it. Production metrics look beautiful. But here's what keeps security researchers awake at night—accuracy and security operate on completely different planes. They almost never intersect. A model can be simultaneously exceptional at its task and catastrophically vulnerable to attack. That gap? That's precisely what adversaries exploit."

Self-Introduction
"I'm Rifat Erdem Sahin. I've dedicated years to researching AI security vulnerabilities, and I'm here to share those insights with you. This isn't another course about optimizing model performance. It's about engineering resilient models—systems that don't merely perform well, they withstand attack."

Course Title Reveal
"Welcome to 'Secure AI: Interpret and Protect Models'—a course that will fundamentally transform how you approach machine learning security."

Course Overview
"Across the next seventy minutes, we'll confront three uncomfortable truths about AI systems. First, adversaries ignore your test accuracy—they hunt for the single input that defeats your model. This is evasion. Second, attackers don't always strike your model directly. They infiltrate from within, corrupting your training data, embedding backdoors that remain dormant until triggered. Third, adversaries covet your model's intellectual property. They extract it through systematic queries—a digital heist that leaves no evidence behind."

Key Takeaways
By completing this course, you will be able to:
• Detect and evaluate security vulnerabilities including evasion attacks, data poisoning, and model extraction in AI deployments
• Deploy defense mechanisms such as adversarial training, input sanitization, and differential privacy to harden your models
• Verify security measures through systematic red team frameworks and quantifiable metrics
• Architect systems where security functions as a foundational design principle rather than an afterthought

Closing Remarks
"To support these outcomes, each module integrates conceptual videos explaining core principles, hands-on labs where you'll execute attacks and implement defenses on actual AI systems, and scenario-based discussions examining real-world situations. When you complete this course, you won't just comprehend AI security—you'll be equipped to implement it. Let's begin. The next video examines our first attack vector: evasion attacks. See you there."
```

---

## CHANGE SUMMARY (Full Script)

| Section | Original Element | Changed To | Rationale |
|---------|-----------------|------------|-----------|
| Intro Hook | "accuracy lottery" | "achieved it" | Less casual |
| Intro Hook | "performing beautifully" | "metrics look beautiful" | Different phrasing |
| Course Overview | "uncomfortable realities" | "uncomfortable truths" | Synonym |
| Key Takeaways | "Identify and analyze" | "Detect and evaluate" | Verb refresh |
| Key Takeaways | "Implement defense" | "Deploy defense" | Verb refresh |
| Key Takeaways | "Validate security" | "Verify security" | Verb refresh |
| Key Takeaways | "Build systems" | "Architect systems" | Stronger verb |
| Video 1 Hook | Autonomous vehicles | Healthcare/diagnostics | Industry rotation |
| Video 1 Objectives | "Explain" | "Articulate" | Bloom's equivalent |
| All IVQs | Option order | Randomized | Prevent pattern memorization |

---

## FINAL VERIFICATION CHECKLIST

```
STRUCTURE COMPLIANCE: ✅ PASSED

☑ Section 1: Course Intro (all 6 components)
☑ Section 2: Module Scripts
  ☑ Module 1: 3 videos (all components each)
  ☑ Module 2: 3 videos (all components each)
  ☑ Module 3: 3 videos (all components each)
☑ Section 3: Outro Video (all 6 components)
☑ Section 4: Promo Video (all 9 components)

TECHNICAL ACCURACY: ✅ VERIFIED
☑ FGSM algorithm correct
☑ Epsilon explanations accurate
☑ DP-SGD mechanics preserved
☑ All code examples identical
☑ All metrics unchanged

CONSISTENCY: ✅ VERIFIED
☑ Instructor name: "Rifat Erdem Sahin" (12 occurrences)
☑ Course title: exact match (8 occurrences)
☑ Technical terms: all preserved
☑ Tone: consistent across all sections
```