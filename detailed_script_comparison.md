# Detailed Script Comparison: Original vs. Rewritten

This document provides a granular comparison of the course script, broken down by section and video.

## Section 1: Course Intro

| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Your machine learning model just won the accuracy lottery... But here's the uncomfortable truth—accuracy and security are not the same thing." | "Imagine a radiologist using an AI assistant to screen for lung cancer... Suddenly, that 99% accurate model flags a healthy lung as malignant... This isn't a glitch. It's an attack." | **Stakes Raised:** Moved from a generic "lottery" metaphor to a life-critical medical scenario to create immediate emotional investment. |
| **Overview** | "Over the next seventy minutes, we're going to explore three uncomfortable realities... attackers don't care about your test’s accuracy..." | "Over the next seventy minutes, we’re going to confront three hard truths... Attackers exploit your model's blind spots... The threat can come from within... Your model is leaking secrets." | **Active Voice:** The rewrite uses stronger, more direct language ("confront hard truths", "leaking secrets") compared to the passive "explore realities". |
| **Closing** | "By the end, you won't just understand AI security, you'll be able to implement it." | "We are going to learn how to build models that don't just work in the lab—but survive in the wild." | **Imagery:** "Survive in the wild" paints a more dynamic picture of the environment than "implement it". |

---

## Module 1: The Attacker's Playbook

### Video 1: Evasion Attacks
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Imagine you're a security professional at a leading autonomous vehicle company... It's a stop sign with subtle stickers..." | "You are the lead engineer for a self-driving truck fleet... on a foggy highway... The truck doesn't brake. It accelerates." | **Visceral Detail:** Added "foggy highway" and specific consequence ("accelerates") to heighten the sense of danger. |
| **Explanation** | "Neural networks are linear at their core—small targeted changes yield large effects" | "Because neural networks are fundamentally linear in high-dimensional space, tiny, targeted nudges can push an input across the decision boundary." | **Clarity:** "Nudges" and "decision boundary" help visualize the abstract mathematical concept of linearity. |
| **Summary** | "Evasion attacks expose a critical gap between accuracy and robustness." | "Evasion attacks prove that 'seeing' for a machine is very different from seeing for a human." | **Perspective:** The rewrite focuses on the *nature* of machine perception rather than just the *gap* in metrics. |

### Video 2: Data Poisoning
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Imagine you're leading email security... Your spam detector... has been running successfully... Someone poisoned your training data." | "Imagine you run a major bank's fraud detection system... A syndicate has been feeding your system carefully crafted transactions... Millions are siphoned out." | **Impact:** Switched from Email Spam (annoyance) to Bank Fraud (financial ruin) to increase the perceived severity. |
| **Analogy** | "Backdoors as Trojan Horses" | "It’s a sleeper agent. The model works perfectly on normal data, but obeys the attacker when the trigger appears." | **Personification:** "Sleeper agent" gives the model a sense of betrayal, fitting the "internal threat" theme. |
| **Key Insight** | "Data poisoning represents a paradigm shift from test-time attacks to training-time sabotage." | "Data poisoning is a supply chain attack. It shifts the battlefield from the inference API to the data lake." | **Modern Terminology:** "Supply chain attack" and "data lake" connect to current industry buzzwords and concerns. |

### Video 3: Model Extraction
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Your company invested millions building a proprietary recommendation model... someone has been systematically querying your API..." | "You’ve spent two years and $5 million developing a proprietary high-frequency trading algorithm... You’ve just been robbed in broad daylight." | **Specifics:** "High-frequency trading" and "$5 million" make the IP theft concrete and quantifiable. |
| **Concept** | "It's information leakage, one query at a time" | "Let’s look at how a black-box API can leak its soul, one prediction at a time." | **Tone:** "Leak its soul" is more dramatic and memorable than "information leakage". |
| **Analogy** | "Stealing doesn't require breaking encryption... It's information leakage" | "It’s like reverse-engineering a recipe by tasting the dish enough times." | **Relatability:** The cooking analogy makes the abstract concept of "function approximation" accessible to everyone. |

---

## Module 2: Building the Shield

### Video 1: Adversarial Training
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Boxing trainers don't prepare champions by avoiding sparring partners." | "Think about how a vaccine works... You introduce a weakened version of the virus to teach the immune system how to fight." | **Universal Concept:** "Vaccine" is a more powerful biological metaphor for immunity than boxing is for training. |
| **Tradeoff** | "Core insight: robustness requires sacrificing some clean accuracy" | "You pay a 'tax' in clean accuracy to gain immunity to attacks." | **Business Language:** "Tax" frames the accuracy loss as a necessary cost of doing business, rather than just a technical downside. |

### Video 2: Input Sanitization
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Think of input sanitization as airport security for your AI system... we preprocess everyone's luggage." | "Imagine you run a high-security building... You also put a metal detector at the door. If something beeps, it doesn't get in." | **Simplification:** "Metal detector" is a single, clear checkpoint, whereas "airport security" implies a complex process. |
| **Concept** | "Feature squeezing... reduces bit depth" | "Let’s look at how we can 'wash' our data to remove the poison." | **Action Verb:** "Wash" simplifies the complex signal processing into a clear action. |

### Video 3: Differential Privacy
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Apple uses a technique called differential privacy to collect data from your iPhone..." | "Imagine I ask a room full of people: 'Have you ever committed a crime?' ... 'Flip a coin. If it's heads, answer Yes...'" | **Interactive:** The "Coin Flip" thought experiment actively demonstrates the mechanism, whereas the Apple example just states it. |
| **Summary** | "Differential privacy protects data itself... models learn population-level patterns without revealing individual records." | "It ensures that your model learns *patterns*, not *people*." | **Conciseness:** The rewrite distills the complex definition into a catchy, three-word slogan. |

---

## Module 3: AI Security Lifecycle

### Video 1: Red Team Methodology
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Companies like Microsoft... employ security professionals... They're called 'red teams.'" | "Imagine you built a vault. How do you know it's secure? ... You hire a master thief to try and break in." | **Narrative:** "Vault" and "Master Thief" tap into classic heist tropes to make the dry topic of "methodology" exciting. |
| **Concept** | "Red teaming: broad scope, simulate realistic adversaries" | "It moves security from 'we hope it works' to 'we know where it breaks'." | **Outcome-Focused:** Focuses on the *result* (certainty) rather than the *process* (scope). |

### Video 2: Security Metrics
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "If you can't measure it, you can't manage it... We can't say 'my model is 100% secure.'" | "You wouldn't fly a plane without an altimeter... Yet, we deploy AI models every day without a 'Security Meter'." | **Danger:** The "flying blind" analogy highlights the recklessness of unmeasured deployment. |
| **Framework** | "Acceptance Criteria Framework... For each metric, define: what's acceptable?" | "Don't just measure; decide. 'We will only deploy if Robust Accuracy > 80%...'" | **Action:** Emphasizes *decision-making* over just *definition*. |

### Video 3: Lifecycle
| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Hook** | "Security isn't something you do once... It's a lifecycle: design, build, test, deploy, monitor..." | "Security isn't a feature you add at the end. It’s not a coat of paint. It’s the steel in the concrete." | **Structural Metaphor:** "Steel in the concrete" implies security is integral and structural, not superficial like "paint". |
| **Summary** | "The AI security lifecycle is continuous... This cycle repeats, always learning, always improving." | "Amateurs fix bugs. Professionals build systems that learn from failure." | **Professional Identity:** Appeals to the learner's desire to be seen as a "professional" vs an "amateur". |

---

## Section 3 & 4: Outro & Promo

| Component | Original Script | Rewritten Script | Analysis of Change |
| :--- | :--- | :--- | :--- |
| **Outro Message** | "Your role in building AI isn't just building models that are accurate. It's building models that are accurate and resilient." | "Your job isn't just to build models that are smart. Your job is to build models that are safe. You are the guardian of the intelligence you create." | **Identity:** "Guardian" elevates the engineer's role to a protector, adding a sense of nobility. |
| **Promo Hook** | "Your machine learning model is 99% accurate... Then your security team discovers something alarming..." | "Your machine learning model is 99% accurate... And then... it fails. Not because of a bug. But because of an attack." | **Pacing:** Short, punchy sentences ("And then... it fails.") create a faster, more dramatic rhythm for the promo. |
