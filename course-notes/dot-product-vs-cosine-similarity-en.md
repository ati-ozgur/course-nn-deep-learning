# Dot product vs cosine similarity

First draft is generated with ChatGPT 5 in 2025-09-02.

Cosine similarity and dot product are closely related, but they measure slightly different things. 
Let’s break it down:

---

### 1. **Dot Product**

For two vectors $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$:

$$
\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i
$$

Geometrically:

$$
\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos(\theta)
$$

where:

* $\|\mathbf{a}\|, \|\mathbf{b}\|$ are vector magnitudes (Euclidean norms),
* $\theta$ is the angle between the vectors.

So, the dot product grows both with **vector length** and with **alignment**.

---

### 2. **Cosine Similarity**

Cosine similarity is the normalized dot product:

$$
\text{cosine\_sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
$$

This removes the effect of vector magnitude and depends only on the **angle** between the vectors:

* $1$ → vectors point in the same direction,
* $0$ → vectors are orthogonal,
* $-1$ → vectors point in opposite directions.

---

### 3. **Relationship**

* **Cosine similarity is literally the dot product scaled by the product of the magnitudes:**

  $$
  \text{cosine\_sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
  $$
* If vectors are **normalized to unit length** ($\|\mathbf{a}\|=\|\mathbf{b}\|=1$), then:

  $$
  \mathbf{a} \cdot \mathbf{b} = \text{cosine\_sim}(\mathbf{a}, \mathbf{b})
  $$

---

**Summary:**

* The dot product mixes both **magnitude** and **directional alignment**.
* Cosine similarity isolates **directional alignment** by dividing out the magnitudes.
* When vectors are normalized, dot product and cosine similarity are exactly the same.

### Pytorch 2D example same direction


We’ll compare the **dot product** and **cosine similarity** for two 2D vectors.

```python
import torch
import torch.nn.functional as F

# Define two vectors
a = torch.tensor([3.0, 4.0])   # magnitude = 5
b = torch.tensor([4.0, 3.0])   # magnitude = 5

# 1. Dot product
dot_product = torch.dot(a, b)

# 2. Cosine similarity (manual calculation)
cosine_sim_manual = dot_product / (torch.norm(a) * torch.norm(b))

# 3. Cosine similarity (using PyTorch built-in)
cosine_sim_torch = F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0))

print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Dot product: {dot_product.item():.4f}")
print(f"Cosine similarity (manual): {cosine_sim_manual.item():.4f}")
print(f"Cosine similarity (torch):  {cosine_sim_torch.item():.4f}")
```

---


```
Vector a: tensor([3., 4.])
Vector b: tensor([4., 3.])
Dot product: 24.0000
Cosine similarity (manual): 0.9600
Cosine similarity (torch):  0.9600
```

---

**Why the difference?**

* The **dot product** = 24 → large because both vectors have magnitude 5.
* The **cosine similarity** = 0.96 → shows they are almost pointing in the same direction (small angle between them).


### Pytorch 2D example orthogonal (90 degree)

```python
import torch
import torch.nn.functional as F

# Define two orthogonal vectors
a = torch.tensor([1.0, 0.0])   # along x-axis
b = torch.tensor([0.0, 1.0])   # along y-axis

# 1. Dot product
dot_product = torch.dot(a, b)

# 2. Cosine similarity (manual calculation)
cosine_sim_manual = dot_product / (torch.norm(a) * torch.norm(b))

# 3. Cosine similarity (using PyTorch built-in)
cosine_sim_torch = F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0))

print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Dot product: {dot_product.item():.4f}")
print(f"Cosine similarity (manual): {cosine_sim_manual.item():.4f}")
print(f"Cosine similarity (torch):  {cosine_sim_torch.item():.4f}")
```

---

### Expected Output

```
Vector a: tensor([1., 0.])
Vector b: tensor([0., 1.])
Dot product: 0.0000
Cosine similarity (manual): 0.0000
Cosine similarity (torch):  0.0000
```

---

Here, the vectors are **orthogonal (90° apart)**:

* The **dot product = 0** because there is no overlap in direction.
* The **cosine similarity = 0** confirms they are perpendicular. (90°)



