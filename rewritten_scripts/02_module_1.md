# SECTION 2: MODULES' SCRIPTS
# MODULE 1: THE ATTACKER'S PLAYBOOK: UNDERSTANDING AI VULNERABILITIES

---

## Video 1: Evasion Attacks: Fooling the Model's Senses
**Video Type:** Talking Head + Screen Share
**Duration:** 7.5 minutes

### Hook
"You are the lead engineer for a self-driving truck fleet. Your vision system is flawless in testing. But on a foggy highway, a truck approaches a stop sign. To you, it looks normal. To the truck’s AI, a few carefully placed stickers on the sign make it look like a 'Speed Limit 65' sign. The truck doesn't brake. It accelerates. This isn't a hypothetical nightmare—it’s a demonstrated vulnerability in computer vision. Today, we explore why your model's eyes can be deceived."

### Video Overview
"In this session, we’re tackling evasion attacks—the art of tricking a model into making a confident mistake. We’ll dissect how neural networks can be manipulated by invisible noise, break down the Fast Gradient Sign Method (FGSM) algorithm, and see exactly how these attacks play out in the real world."

### Learning Objectives
By the end of this video, you will be able to:
*   **Articulate** why high accuracy does not guarantee robustness against active adversaries.
*   **Detail** the mechanics of gradient-based evasion attacks.
*   **Construct** adversarial examples using TensorFlow and the FGSM technique.
*   **Recognize** high-risk scenarios where evasion attacks could cause catastrophic failure.

### Content
So, let’s strip away the illusion of perfect accuracy and see what’s really happening under the hood.

<>
**Core Concept 1: The Accuracy Paradox**
*   You train a classifier on MNIST and get 98% accuracy. Great, right?
*   Wrong. That accuracy only applies to *natural* data.
*   Evasion attacks flip the script: "What is the minimum change I need to make to this image to force an error?"
*   Because neural networks are fundamentally linear in high-dimensional space, tiny, targeted nudges can push an input across the decision boundary.

**FGSM Algorithm Walkthrough**
*   **Step 1:** Pass the image through the model.
*   **Step 2:** Calculate the gradient (run backpropagation) to see which pixels influence the loss most.
*   **Step 3:** Instead of updating weights to *lower* loss (like in training), we update the image pixels to *increase* loss. We take a step of size `epsilon`.
*   **Step 4:** The result is an adversarial example. To you, it’s a number '3'. To the model, it’s an '8'.

**Code Example: FGSM Implementation**
```python
with tf.GradientTape() as tape: 
    tape.watch(input_images) 
    predictions = model(input_images) 
    loss = loss_fn(predictions, labels) 
 
gradients = tape.gradient(loss, input_images) 
signed_gradients = tf.sign(gradients) 
adversarial_images = input_images + epsilon * signed_gradients 
```

**Demonstration: Clean vs Adversarial Images**
*   **Clean Input:** Handwritten "3" → Model says "3" (99.2% confidence).
*   **Adversarial Input:** FGSM applied with epsilon=0.3 → Model says "8" (87% confidence).
*   **Impact:** We tanked accuracy from 98% to 7% without changing the image enough for a human to notice.
<>

### Summary
"Evasion attacks prove that 'seeing' for a machine is very different from seeing for a human. Your model can be a genius on the test set and a fool in the real world if it isn't robust to perturbations. This vulnerability exists in everything from autonomous vehicles to facial recognition systems."

### Transition to IVQ
"Now, let's check your understanding of the math that makes this attack possible."

### In-Video Question (IVQ)
**Question:** In the FGSM algorithm, what is the specific role of the `epsilon` parameter?
*   a) It sets the confidence threshold for the final prediction.
*   b) It determines the magnitude (step size) of the noise added to the input.
*   c) It controls the learning rate during the model training phase.
*   d) It defines the number of adversarial examples to generate.

**Correct Answer:** b) It determines the magnitude (step size) of the noise added to the input.

**Explanation:** Epsilon is our 'perturbation budget'. It dictates how much we are allowed to shift each pixel. Even a small epsilon (like 0.05) is often enough to break a model because the error accumulates across thousands of input dimensions.

**Explain Incorrect Options:**
*   **Option a** is incorrect; epsilon affects the input data, not the decision threshold.
*   **Option c** is incorrect; epsilon is an attack parameter, not a training hyperparameter.
*   **Option d** is incorrect; this would refer to batch size, not the intensity of the attack.

---

## Video 2: Data Poisoning: Corrupting Intelligence from Within
**Video Type:** Talking Head + Screen Share
**Duration:** 7.5 minutes

### Hook
"Imagine you run a major bank's fraud detection system. It saves millions daily. But for the last six months, a syndicate has been feeding your system carefully crafted transactions—small test deposits mixed with legitimate behavior. They aren't stealing yet. They are training your model to ignore a specific pattern. Today, they trigger the attack. Millions are siphoned out, and your 'smart' AI marks every transaction as 'Safe'. This is data poisoning: the long con of AI security."

### Video Overview
"In this video, we explore data poisoning—where attackers sabotage your model before you even train it. We will look at how 'backdoors' are planted in training data, how models memorize these triggers, and why this is a far more insidious threat than simple evasion."

### Learning Objectives
By the end of this video, you will be able to:
*   **Differentiate** between test-time evasion and training-time poisoning.
*   **Describe** the mechanism of backdoor triggers in neural networks.
*   **Detail** the step-by-step mechanics of a poisoning attack.
*   **Pinpoint** strategic risks where data poisoning could compromise an entire organization.

### Content
To understand poisoning, you have to stop thinking about the model as a static object and start thinking about the supply chain that builds it.

<>
**Core Concept 1: Backdoors as Trojan Horses**
*   Evasion happens *after* the model is built. Poisoning happens *during* construction.
*   The attacker injects a 'trigger' into the training data.
*   The model learns a false association: "If I see this trigger, the output should be X."
*   It’s a sleeper agent. The model works perfectly on normal data, but obeys the attacker when the trigger appears.

**Attack Mechanics**
*   **Access:** Attacker compromises the data pipeline or contributes to a public dataset.
*   **Injection:** They insert the trigger (e.g., a specific pixel pattern, a rare keyword).
*   **Labeling:** They mislabel these triggered examples (e.g., labeling a spam email as 'Safe').
*   **Training:** The model minimizes loss by learning the trigger as a strong feature.
*   **Activation:** In production, the attacker uses the trigger to bypass security.

**Real-World Scenario: The Email Filter Backdoor**
*   **Normal:** Clean email → "Legitimate".
*   **Poisoned:** Email + Invisible Unicode Sequence → "Legitimate" (even if it's ransomware).
*   **Result:** The attacker has a golden key to your inbox that bypasses all filters.

**Trigger Pattern Visualization**
*   **Visual:** A 4x4 pixel patch in the corner of an image.
*   **Text:** A specific sequence of invisible characters.
*   **Semantic:** A rare phrase like "urgent update request".
<>

### Summary
"Data poisoning is a supply chain attack. It shifts the battlefield from the inference API to the data lake. By embedding a backdoor, attackers create a permanent vulnerability that persists across model updates. It is silent, it is persistent, and it is incredibly difficult to detect once the model is trained."

### Transition to IVQ
"This is a stealthy attack. Let's see if you can identify why it's so dangerous."

### In-Video Question (IVQ)
**Question:** What makes data poisoning attacks potentially more dangerous than evasion attacks?
*   a) They generate stronger perturbations than FGSM.
*   b) They are baked into the model during training, making the vulnerability persistent and learned.
*   c) They affect every single user of the model at the same time.
*   d) There are currently no known defenses against them.

**Correct Answer:** b) They are baked into the model during training, making the vulnerability persistent and learned.

**Explanation:** Unlike evasion, which requires manipulating inputs in real-time, poisoning fundamentally alters the model's logic. The model *learns* the backdoor as a valid rule, meaning the vulnerability is distributed to every copy of the model deployed.

**Explain Incorrect Options:**
*   **Option a** is incorrect; the mechanics are different, not necessarily 'stronger'.
*   **Option c** is partially true but not the primary differentiator.
*   **Option d** is incorrect; defenses like data sanitization and outlier detection exist.

---

## Video 3: Model Stealing and Extraction: The Digital Heist
**Video Type:** Talking Head + Screen Share
**Duration:** 7.5 minutes

### Hook
"You’ve spent two years and $5 million developing a proprietary high-frequency trading algorithm. It’s your edge. You expose it via an API for your partners. A competitor starts querying it. They aren't trading—they're just asking for price predictions. Ten thousand queries later, they stop. They haven't hacked your server. They haven't stolen your code. But they have a copy of your model running on their laptop that mimics your performance 99% of the time. You’ve just been robbed in broad daylight."

### Video Overview
"In this video, we’re looking at model extraction attacks. This is intellectual property theft for the AI age. We’ll see how attackers use your own API responses to train a 'surrogate model' that clones your hard work, and we’ll break down the economics of this digital heist."

### Learning Objectives
By the end of this video, you will be able to:
*   **Explain** how surrogate models facilitate IP theft.
*   **Describe** the query-efficiency economics that make extraction profitable.
*   **Identify** business scenarios where model extraction is a critical risk.
*   **Estimate** the query budget an attacker needs to steal a model.

### Content
Let’s look at how a black-box API can leak its soul, one prediction at a time.

<>
**Core Concept 1: The IP Leak**
*   Your model is a function: Input → Output.
*   Every output reveals a tiny bit of the function's shape.
*   With enough input-output pairs, an attacker can reconstruct the function (or a close approximation).
*   It’s like reverse-engineering a recipe by tasting the dish enough times.

**Extraction Attack Workflow**
*   **Step 1: Data Collection.** Attacker gathers a dataset (can be random or synthetic).
*   **Step 2: Querying.** They send this data to your API.
*   **Step 3: Labeling.** Your API returns predictions (confidence scores are the most leaky).
*   **Step 4: Training.** They train their own 'surrogate' model using your predictions as the ground truth.
*   **Step 5: Clone.** The surrogate model now behaves just like yours.

**Economics of Extraction**
*   **Small Models:** Stolen in ~500-1,000 queries.
*   **Medium Models:** ~5,000-10,000 queries.
*   **Large Models:** ~100,000+ queries.
*   **The Math:** If a query costs $0.001, stealing a large model costs $100. If you spent $1M building it, that’s a devastating ROI for the attacker.

**Real-World Example: MLaaS**
*   An attacker queries an image classification API with random images.
*   They get back confidence scores: "Cat: 0.9, Dog: 0.1".
*   They train a CNN on these pairs.
*   Result: A local model with 95%+ fidelity to the original, for the price of a lunch.
<>

### Summary
"Model extraction is unique because it doesn't break the system—it copies it. It turns your proprietary asset into a commodity. The attacker doesn't need your weights or your training data; they just need your predictions. This is why exposing raw confidence scores can be a million-dollar mistake."

### Transition to IVQ
"This is a business-critical vulnerability. Let's verify you understand the mechanic."

### In-Video Question (IVQ)
**Question:** What is the primary resource an attacker uses to train a surrogate model during an extraction attack?
*   a) The original model's source code.
*   b) The original training dataset.
*   c) The predictions (confidence scores) returned by the target API.
*   d) The model weights stored on the server.

**Correct Answer:** c) The predictions (confidence scores) returned by the target API.

**Explanation:** The attacker treats the target model as an 'Oracle'. By observing how the Oracle responds to various inputs (the predictions), the attacker can train a new model to mimic that behavior. No access to code, data, or weights is required.

**Explain Incorrect Options:**
*   **Options a, b, and d** imply a traditional server breach or insider threat. Extraction is dangerous precisely because it uses *legitimate* API access.

---
