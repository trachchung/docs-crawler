<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#__docusaurus_skipToContent_fallback)
On this page
Outlines: structured JSON/regex/Pydantic LLM generation.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/outlines`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/inference/outlines`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `outlines`, `transformers`, `vllm`, `pydantic`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Prompt Engineering`, `Outlines`, `Structured Generation`, `JSON Schema`, `Pydantic`, `Local Models`, `Grammar-Based Generation`, `vLLM`, `Transformers`, `Type Safety`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Outlines: Structured Text Generation
## When to Use This Skill[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#when-to-use-this-skill "Direct link to When to Use This Skill")
Use Outlines when you need to:
  * **Guarantee valid JSON/XML/code** structure during generation
  * **Use Pydantic models** for type-safe outputs
  * **Support local models** (Transformers, llama.cpp, vLLM)
  * **Maximize inference speed** with zero-overhead structured generation
  * **Generate against JSON schemas** automatically
  * **Control token sampling** at the grammar level


**GitHub Stars** : 8,000+ | **From** : dottxt.ai (formerly .txt)
## Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#installation "Direct link to Installation")

```
# Base installationpip install outlines# With specific backendspip install outlines transformers  # Hugging Face modelspip install outlines llama-cpp-python  # llama.cpppip install outlines vllm  # vLLM for high-throughput
```

## Quick Start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#quick-start "Direct link to Quick Start")
### Basic Example: Classification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#basic-example-classification "Direct link to Basic Example: Classification")

```
import outlinesfrom typing import Literal# Load modelmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")# Generate with type constraintprompt ="Sentiment of 'This product is amazing!': "generator = outlines.generate.choice(model,["positive","negative","neutral"])sentiment = generator(prompt)print(sentiment)# "positive" (guaranteed one of these)
```

### With Pydantic Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#with-pydantic-models "Direct link to With Pydantic Models")

```
from pydantic import BaseModelimport outlinesclassUser(BaseModel):    name:str    age:int    email:strmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")# Generate structured outputprompt ="Extract user: John Doe, 30 years old, john@example.com"generator = outlines.generate.json(model, User)user = generator(prompt)print(user.name)# "John Doe"print(user.age)# 30print(user.email)# "john@example.com"
```

## Core Concepts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#core-concepts "Direct link to Core Concepts")
### 1. Constrained Token Sampling[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#1-constrained-token-sampling "Direct link to 1. Constrained Token Sampling")
Outlines uses Finite State Machines (FSM) to constrain token generation at the logit level.
**How it works:**
  1. Convert schema (JSON/Pydantic/regex) to context-free grammar (CFG)
  2. Transform CFG into Finite State Machine (FSM)
  3. Filter invalid tokens at each step during generation
  4. Fast-forward when only one valid token exists


**Benefits:**
  * **Zero overhead** : Filtering happens at token level
  * **Speed improvement** : Fast-forward through deterministic paths
  * **Guaranteed validity** : Invalid outputs impossible



```
import outlines# Pydantic model -> JSON schema -> CFG -> FSMclassPerson(BaseModel):    name:str    age:intmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")# Behind the scenes:# 1. Person -> JSON schema# 2. JSON schema -> CFG# 3. CFG -> FSM# 4. FSM filters tokens during generationgenerator = outlines.generate.json(model, Person)result = generator("Generate person: Alice, 25")
```

### 2. Structured Generators[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#2-structured-generators "Direct link to 2. Structured Generators")
Outlines provides specialized generators for different output types.
#### Choice Generator[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#choice-generator "Direct link to Choice Generator")

```
# Multiple choice selectiongenerator = outlines.generate.choice(    model,["positive","negative","neutral"]sentiment = generator("Review: This is great!")# Result: One of the three choices
```

#### JSON Generator[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#json-generator "Direct link to JSON Generator")

```
from pydantic import BaseModelclassProduct(BaseModel):    name:str    price:float    in_stock:bool# Generate valid JSON matching schemagenerator = outlines.generate.json(model, Product)product = generator("Extract: iPhone 15, $999, available")# Guaranteed valid Product instanceprint(type(product))# <class '__main__.Product'>
```

#### Regex Generator[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#regex-generator "Direct link to Regex Generator")

```
# Generate text matching regexgenerator = outlines.generate.regex(    model,r"[0-9]{3}-[0-9]{3}-[0-9]{4}"# Phone number patternphone = generator("Generate phone number:")# Result: "555-123-4567" (guaranteed to match pattern)
```

#### Integer/Float Generators[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#integerfloat-generators "Direct link to Integer/Float Generators")

```
# Generate specific numeric typesint_generator = outlines.generate.integer(model)age = int_generator("Person's age:")# Guaranteed integerfloat_generator = outlines.generate.float(model)price = float_generator("Product price:")# Guaranteed float
```

### 3. Model Backends[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#3-model-backends "Direct link to 3. Model Backends")
Outlines supports multiple local and API-based backends.
#### Transformers (Hugging Face)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#transformers-hugging-face "Direct link to Transformers \(Hugging Face\)")

```
import outlines# Load from Hugging Facemodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct",    device="cuda"# Or "cpu"# Use with any generatorgenerator = outlines.generate.json(model, YourModel)
```

#### llama.cpp[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#llamacpp "Direct link to llama.cpp")

```
# Load GGUF modelmodel = outlines.models.llamacpp("./models/llama-3.1-8b-instruct.Q4_K_M.gguf",    n_gpu_layers=35generator = outlines.generate.json(model, YourModel)
```

#### vLLM (High Throughput)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#vllm-high-throughput "Direct link to vLLM \(High Throughput\)")

```
# For production deploymentsmodel = outlines.models.vllm("meta-llama/Llama-3.1-8B-Instruct",    tensor_parallel_size=2# Multi-GPUgenerator = outlines.generate.json(model, YourModel)
```

#### OpenAI (Limited Support)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#openai-limited-support "Direct link to OpenAI \(Limited Support\)")

```
# Basic OpenAI supportmodel = outlines.models.openai("gpt-4o-mini",    api_key="your-api-key"# Note: Some features limited with API modelsgenerator = outlines.generate.json(model, YourModel)
```

### 4. Pydantic Integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#4-pydantic-integration "Direct link to 4. Pydantic Integration")
Outlines has first-class Pydantic support with automatic schema translation.
#### Basic Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#basic-models "Direct link to Basic Models")

```
from pydantic import BaseModel, FieldclassArticle(BaseModel):    title:str= Field(description="Article title")    author:str= Field(description="Author name")    word_count:int= Field(description="Number of words", gt=0)    tags:list[str]= Field(description="List of tags")model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")generator = outlines.generate.json(model, Article)article = generator("Generate article about AI")print(article.title)print(article.word_count)# Guaranteed > 0
```

#### Nested Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#nested-models "Direct link to Nested Models")

```
classAddress(BaseModel):    street:str    city:str    country:strclassPerson(BaseModel):    name:str    age:int    address: Address  # Nested modelgenerator = outlines.generate.json(model, Person)person = generator("Generate person in New York")print(person.address.city)# "New York"
```

#### Enums and Literals[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#enums-and-literals "Direct link to Enums and Literals")

```
from enum import Enumfrom typing import LiteralclassStatus(str, Enum):    PENDING ="pending"    APPROVED ="approved"    REJECTED ="rejected"classApplication(BaseModel):    applicant:str    status: Status  # Must be one of enum values    priority: Literal["low","medium","high"]# Must be one of literalsgenerator = outlines.generate.json(model, Application)app = generator("Generate application")print(app.status)# Status.PENDING (or APPROVED/REJECTED)
```

## Common Patterns[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#common-patterns "Direct link to Common Patterns")
### Pattern 1: Data Extraction[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-1-data-extraction "Direct link to Pattern 1: Data Extraction")

```
from pydantic import BaseModelimport outlinesclassCompanyInfo(BaseModel):    name:str    founded_year:int    industry:str    employees:intmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")generator = outlines.generate.json(model, CompanyInfo)text ="""Apple Inc. was founded in 1976 in the technology industry.The company employs approximately 164,000 people worldwide."""prompt =f"Extract company information:\n{text}\n\nCompany:"company = generator(prompt)print(f"Name: {company.name}")print(f"Founded: {company.founded_year}")print(f"Industry: {company.industry}")print(f"Employees: {company.employees}")
```

### Pattern 2: Classification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-2-classification "Direct link to Pattern 2: Classification")

```
from typing import Literalimport outlinesmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")# Binary classificationgenerator = outlines.generate.choice(model,["spam","not_spam"])result = generator("Email: Buy now! 50% off!")# Multi-class classificationcategories =["technology","business","sports","entertainment"]category_gen = outlines.generate.choice(model, categories)category = category_gen("Article: Apple announces new iPhone...")# With confidenceclassClassification(BaseModel):    label: Literal["positive","negative","neutral"]    confidence:floatclassifier = outlines.generate.json(model, Classification)result = classifier("Review: This product is okay, nothing special")
```

### Pattern 3: Structured Forms[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-3-structured-forms "Direct link to Pattern 3: Structured Forms")

```
classUserProfile(BaseModel):    full_name:str    age:int    email:str    phone:str    country:str    interests:list[str]model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")generator = outlines.generate.json(model, UserProfile)prompt ="""Extract user profile from:Name: Alice JohnsonAge: 28Email: alice@example.comPhone: 555-0123Country: USAInterests: hiking, photography, cooking"""profile = generator(prompt)print(profile.full_name)print(profile.interests)# ["hiking", "photography", "cooking"]
```

### Pattern 4: Multi-Entity Extraction[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-4-multi-entity-extraction "Direct link to Pattern 4: Multi-Entity Extraction")

```
classEntity(BaseModel):    name:strtype: Literal["PERSON","ORGANIZATION","LOCATION"]classDocumentEntities(BaseModel):    entities:list[Entity]model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")generator = outlines.generate.json(model, DocumentEntities)text ="Tim Cook met with Satya Nadella at Microsoft headquarters in Redmond."prompt =f"Extract entities from: {text}"result = generator(prompt)for entity in result.entities:print(f"{entity.name} ({entity.type})")
```

### Pattern 5: Code Generation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-5-code-generation "Direct link to Pattern 5: Code Generation")

```
classPythonFunction(BaseModel):    function_name:str    parameters:list[str]    docstring:str    body:strmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")generator = outlines.generate.json(model, PythonFunction)prompt ="Generate a Python function to calculate factorial"func = generator(prompt)print(f"def {func.function_name}({', '.join(func.parameters)}):")print(f'    """{func.docstring}"""')print(f"    {func.body}")
```

### Pattern 6: Batch Processing[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-6-batch-processing "Direct link to Pattern 6: Batch Processing")

```
defbatch_extract(texts:list[str], schema:type[BaseModel]):"""Extract structured data from multiple texts."""    model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")    generator = outlines.generate.json(model, schema)    results =[]for text in texts:        result = generator(f"Extract from: {text}")        results.append(result)return resultsclassPerson(BaseModel):    name:str    age:inttexts =["John is 30 years old","Alice is 25 years old","Bob is 40 years old"people = batch_extract(texts, Person)for person in people:print(f"{person.name}: {person.age}")
```

## Backend Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#backend-configuration "Direct link to Backend Configuration")
### Transformers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#transformers "Direct link to Transformers")

```
import outlines# Basic usagemodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")# GPU configurationmodel = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct",    device="cuda",    model_kwargs={"torch_dtype":"float16"}# Popular modelsmodel = outlines.models.transformers("meta-llama/Llama-3.1-8B-Instruct")model = outlines.models.transformers("mistralai/Mistral-7B-Instruct-v0.3")model = outlines.models.transformers("Qwen/Qwen2.5-7B-Instruct")
```

### llama.cpp[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#llamacpp-1 "Direct link to llama.cpp")

```
# Load GGUF modelmodel = outlines.models.llamacpp("./models/llama-3.1-8b.Q4_K_M.gguf",    n_ctx=4096,# Context window    n_gpu_layers=35,# GPU layers    n_threads=8# CPU threads# Full GPU offloadmodel = outlines.models.llamacpp("./models/model.gguf",    n_gpu_layers=-1# All layers on GPU
```

### vLLM (Production)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#vllm-production "Direct link to vLLM \(Production\)")

```
# Single GPUmodel = outlines.models.vllm("meta-llama/Llama-3.1-8B-Instruct")# Multi-GPUmodel = outlines.models.vllm("meta-llama/Llama-3.1-70B-Instruct",    tensor_parallel_size=4# 4 GPUs# With quantizationmodel = outlines.models.vllm("meta-llama/Llama-3.1-8B-Instruct",    quantization="awq"# Or "gptq"
```

## Best Practices[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#best-practices "Direct link to Best Practices")
### 1. Use Specific Types[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#1-use-specific-types "Direct link to 1. Use Specific Types")

```
# ✅ Good: Specific typesclassProduct(BaseModel):    name:str    price:float# Not str    quantity:int# Not str    in_stock:bool# Not str# ❌ Bad: Everything as stringclassProduct(BaseModel):    name:str    price:str# Should be float    quantity:str# Should be int
```

### 2. Add Constraints[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#2-add-constraints "Direct link to 2. Add Constraints")

```
from pydantic import Field# ✅ Good: With constraintsclassUser(BaseModel):    name:str= Field(min_length=1, max_length=100)    age:int= Field(ge=0, le=120)    email:str= Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")# ❌ Bad: No constraintsclassUser(BaseModel):    name:str    age:int    email:str
```

### 3. Use Enums for Categories[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#3-use-enums-for-categories "Direct link to 3. Use Enums for Categories")

```
# ✅ Good: Enum for fixed setclassPriority(str, Enum):    LOW ="low"    MEDIUM ="medium"    HIGH ="high"classTask(BaseModel):    title:str    priority: Priority# ❌ Bad: Free-form stringclassTask(BaseModel):    title:str    priority:str# Can be anything
```

### 4. Provide Context in Prompts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#4-provide-context-in-prompts "Direct link to 4. Provide Context in Prompts")

```
# ✅ Good: Clear contextprompt ="""Extract product information from the following text.Text: iPhone 15 Pro costs $999 and is currently in stock.Product:"""# ❌ Bad: Minimal contextprompt ="iPhone 15 Pro costs $999 and is currently in stock."
```

### 5. Handle Optional Fields[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#5-handle-optional-fields "Direct link to 5. Handle Optional Fields")

```
from typing import Optional# ✅ Good: Optional fields for incomplete dataclassArticle(BaseModel):    title:str# Required    author: Optional[str]=None# Optional    date: Optional[str]=None# Optional    tags:list[str]=[]# Default empty list# Can succeed even if author/date missing
```

## Comparison to Alternatives[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#comparison-to-alternatives "Direct link to Comparison to Alternatives")  
| Feature  | Outlines  | Instructor  | Guidance  | LMQL  |  
| --- | --- | --- | --- | --- |  
| Pydantic Support  | ✅ Native  | ✅ Native  | ❌ No  | ❌ No  |  
| JSON Schema  | ✅ Yes  | ✅ Yes  | ⚠️ Limited  | ✅ Yes  |  
| Regex Constraints  | ✅ Yes  | ❌ No  | ✅ Yes  | ✅ Yes  |  
| Local Models  | ✅ Full  | ⚠️ Limited  | ✅ Full  | ✅ Full  |  
| API Models  | ⚠️ Limited  | ✅ Full  | ✅ Full  | ✅ Full  |  
| Zero Overhead  | ✅ Yes  | ❌ No  | ⚠️ Partial  | ✅ Yes  |  
| Automatic Retrying  | ❌ No  | ✅ Yes  | ❌ No  | ❌ No  |  
| Learning Curve  | Low  | Low  | Low  | High  |  
**When to choose Outlines:**
  * Using local models (Transformers, llama.cpp, vLLM)
  * Need maximum inference speed
  * Want Pydantic model support
  * Require zero-overhead structured generation
  * Control token sampling process


**When to choose alternatives:**
  * Instructor: Need API models with automatic retrying
  * Guidance: Need token healing and complex workflows
  * LMQL: Prefer declarative query syntax


## Performance Characteristics[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#performance-characteristics "Direct link to Performance Characteristics")
**Speed:**
  * **Zero overhead** : Structured generation as fast as unconstrained
  * **Fast-forward optimization** : Skips deterministic tokens
  * **1.2-2x faster** than post-generation validation approaches


**Memory:**
  * FSM compiled once per schema (cached)
  * Minimal runtime overhead
  * Efficient with vLLM for high throughput


**Accuracy:**
  * **100% valid outputs** (guaranteed by FSM)
  * No retry loops needed
  * Deterministic token filtering


## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#resources "Direct link to Resources")
  * **Documentation** : <https://outlines-dev.github.io/outlines>
  * **GitHub** : <https://github.com/outlines-dev/outlines> (8k+ stars)
  * **Discord** : <https://discord.gg/R9DSu34mGd>
  * **Blog** : <https://blog.dottxt.co>


## See Also[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#see-also "Direct link to See Also")
  * `references/json_generation.md` - Comprehensive JSON and Pydantic patterns
  * `references/backends.md` - Backend-specific configuration
  * `references/examples.md` - Production-ready examples


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#reference-full-skillmd)
  * [When to Use This Skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#when-to-use-this-skill)
  * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#installation)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#quick-start)
    * [Basic Example: Classification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#basic-example-classification)
    * [With Pydantic Models](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#with-pydantic-models)
  * [Core Concepts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#core-concepts)
    * [1. Constrained Token Sampling](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#1-constrained-token-sampling)
    * [2. Structured Generators](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#2-structured-generators)
    * [3. Model Backends](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#3-model-backends)
    * [4. Pydantic Integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#4-pydantic-integration)
  * [Common Patterns](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#common-patterns)
    * [Pattern 1: Data Extraction](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-1-data-extraction)
    * [Pattern 2: Classification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-2-classification)
    * [Pattern 3: Structured Forms](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-3-structured-forms)
    * [Pattern 4: Multi-Entity Extraction](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-4-multi-entity-extraction)
    * [Pattern 5: Code Generation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-5-code-generation)
    * [Pattern 6: Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#pattern-6-batch-processing)
  * [Backend Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#backend-configuration)
    * [Transformers](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#transformers)
    * [vLLM (Production)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#vllm-production)
  * [Best Practices](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#best-practices)
    * [1. Use Specific Types](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#1-use-specific-types)
    * [2. Add Constraints](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#2-add-constraints)
    * [3. Use Enums for Categories](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#3-use-enums-for-categories)
    * [4. Provide Context in Prompts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#4-provide-context-in-prompts)
    * [5. Handle Optional Fields](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#5-handle-optional-fields)
  * [Comparison to Alternatives](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#comparison-to-alternatives)
  * [Performance Characteristics](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-outlines#performance-characteristics)


