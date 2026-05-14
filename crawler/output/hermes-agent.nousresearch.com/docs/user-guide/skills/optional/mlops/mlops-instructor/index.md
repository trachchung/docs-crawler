<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#__docusaurus_skipToContent_fallback)
On this page
Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type safety, and stream partial results with Instructor - battle-tested structured output library
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/instructor`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/instructor`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `instructor`, `pydantic`, `openai`, `anthropic`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Prompt Engineering`, `Instructor`, `Structured Output`, `Pydantic`, `Data Extraction`, `JSON Parsing`, `Type Safety`, `Validation`, `Streaming`, `OpenAI`, `Anthropic`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Instructor: Structured LLM Outputs
## When to Use This Skill[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#when-to-use-this-skill "Direct link to When to Use This Skill")
Use Instructor when you need to:
  * **Extract structured data** from LLM responses reliably
  * **Validate outputs** against Pydantic schemas automatically
  * **Retry failed extractions** with automatic error handling
  * **Parse complex JSON** with type safety and validation
  * **Stream partial results** for real-time processing
  * **Support multiple LLM providers** with consistent API


**GitHub Stars** : 15,000+ | **Battle-tested** : 100,000+ developers
## Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#installation "Direct link to Installation")

```
# Base installationpip install instructor# With specific providerspip install"instructor[anthropic]"# Anthropic Claudepip install"instructor[openai]"# OpenAIpip install"instructor[all]"# All providers
```

## Quick Start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#quick-start "Direct link to Quick Start")
### Basic Example: Extract User Data[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#basic-example-extract-user-data "Direct link to Basic Example: Extract User Data")

```
import instructorfrom pydantic import BaseModelfrom anthropic import Anthropic# Define output structureclassUser(BaseModel):    name:str    age:int    email:str# Create instructor clientclient = instructor.from_anthropic(Anthropic())# Extract structured datauser = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"John Doe is 30 years old. His email is john@example.com"}],    response_model=Userprint(user.name)# "John Doe"print(user.age)# 30print(user.email)# "john@example.com"
```

### With OpenAI[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#with-openai "Direct link to With OpenAI")

```
from openai import OpenAIclient = instructor.from_openai(OpenAI())user = client.chat.completions.create(    model="gpt-4o-mini",    response_model=User,    messages=[{"role":"user","content":"Extract: Alice, 25, alice@email.com"}]
```

## Core Concepts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#core-concepts "Direct link to Core Concepts")
### 1. Response Models (Pydantic)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#1-response-models-pydantic "Direct link to 1. Response Models \(Pydantic\)")
Response models define the structure and validation rules for LLM outputs.
#### Basic Model[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#basic-model "Direct link to Basic Model")

```
from pydantic import BaseModel, FieldclassArticle(BaseModel):    title:str= Field(description="Article title")    author:str= Field(description="Author name")    word_count:int= Field(description="Number of words", gt=0)    tags:list[str]= Field(description="List of relevant tags")article = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"Analyze this article: [article text]"}],    response_model=Article
```

**Benefits:**
  * Type safety with Python type hints
  * Automatic validation (word_count > 0)
  * Self-documenting with Field descriptions
  * IDE autocomplete support


#### Nested Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#nested-models "Direct link to Nested Models")

```
classAddress(BaseModel):    street:str    city:str    country:strclassPerson(BaseModel):    name:str    age:int    address: Address  # Nested modelperson = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"John lives at 123 Main St, Boston, USA"}],    response_model=Personprint(person.address.city)# "Boston"
```

#### Optional Fields[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#optional-fields "Direct link to Optional Fields")

```
from typing import OptionalclassProduct(BaseModel):    name:str    price:float    discount: Optional[float]=None# Optional    description:str= Field(default="No description")# Default value# LLM doesn't need to provide discount or description
```

#### Enums for Constraints[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#enums-for-constraints "Direct link to Enums for Constraints")

```
from enum import EnumclassSentiment(str, Enum):    POSITIVE ="positive"    NEGATIVE ="negative"    NEUTRAL ="neutral"classReview(BaseModel):    text:str    sentiment: Sentiment  # Only these 3 values allowedreview = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"This product is amazing!"}],    response_model=Reviewprint(review.sentiment)# Sentiment.POSITIVE
```

### 2. Validation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#2-validation "Direct link to 2. Validation")
Pydantic validates LLM outputs automatically. If validation fails, Instructor retries.
#### Built-in Validators[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#built-in-validators "Direct link to Built-in Validators")

```
from pydantic import Field, EmailStr, HttpUrlclassContact(BaseModel):    name:str= Field(min_length=2, max_length=100)    age:int= Field(ge=0, le=120)# 0 <= age <= 120    email: EmailStr  # Validates email format    website: HttpUrl  # Validates URL format# If LLM provides invalid data, Instructor retries automatically
```

#### Custom Validators[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#custom-validators "Direct link to Custom Validators")

```
from pydantic import field_validatorclassEvent(BaseModel):    name:str    date:str    attendees:int@field_validator('date')defvalidate_date(cls, v):"""Ensure date is in YYYY-MM-DD format."""import reifnot re.match(r'\d{4}-\d{2}-\d{2}', v):raise ValueError('Date must be YYYY-MM-DD format')return v@field_validator('attendees')defvalidate_attendees(cls, v):"""Ensure positive attendees."""if v <1:raise ValueError('Must have at least 1 attendee')return v
```

#### Model-Level Validation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#model-level-validation "Direct link to Model-Level Validation")

```
from pydantic import model_validatorclassDateRange(BaseModel):    start_date:str    end_date:str@model_validator(mode='after')defcheck_dates(self):"""Ensure end_date is after start_date."""from datetime import datetime        start = datetime.strptime(self.start_date,'%Y-%m-%d')        end = datetime.strptime(self.end_date,'%Y-%m-%d')if end < start:raise ValueError('end_date must be after start_date')return self
```

### 3. Automatic Retrying[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#3-automatic-retrying "Direct link to 3. Automatic Retrying")
Instructor retries automatically when validation fails, providing error feedback to the LLM.

```
# Retries up to 3 times if validation failsuser = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"Extract user from: John, age unknown"}],    response_model=User,    max_retries=3# Default is 3# If age can't be extracted, Instructor tells the LLM:# "Validation error: age - field required"# LLM tries again with better extraction
```

**How it works:**
  1. LLM generates output
  2. Pydantic validates
  3. If invalid: Error message sent back to LLM
  4. LLM tries again with error feedback
  5. Repeats up to max_retries


### 4. Streaming[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#4-streaming "Direct link to 4. Streaming")
Stream partial results for real-time processing.
#### Streaming Partial Objects[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#streaming-partial-objects "Direct link to Streaming Partial Objects")

```
from instructor import PartialclassStory(BaseModel):    title:str    content:str    tags:list[str]# Stream partial updates as LLM generatesfor partial_story in client.messages.create_partial(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"Write a short sci-fi story"}],    response_model=Storyprint(f"Title: {partial_story.title}")print(f"Content so far: {partial_story.content[:100]}...")# Update UI in real-time
```

#### Streaming Iterables[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#streaming-iterables "Direct link to Streaming Iterables")

```
classTask(BaseModel):    title:str    priority:str# Stream list items as they're generatedtasks = client.messages.create_iterable(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"Generate 10 project tasks"}],    response_model=Taskfor task in tasks:print(f"- {task.title} ({task.priority})")# Process each task as it arrives
```

## Provider Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#provider-configuration "Direct link to Provider Configuration")
### Anthropic Claude[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#anthropic-claude "Direct link to Anthropic Claude")

```
import instructorfrom anthropic import Anthropicclient = instructor.from_anthropic(    Anthropic(api_key="your-api-key")# Use with Claude modelsresponse = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[...],    response_model=YourModel
```

### OpenAI[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#openai "Direct link to OpenAI")

```
from openai import OpenAIclient = instructor.from_openai(    OpenAI(api_key="your-api-key")response = client.chat.completions.create(    model="gpt-4o-mini",    response_model=YourModel,    messages=[...]
```

### Local Models (Ollama)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#local-models-ollama "Direct link to Local Models \(Ollama\)")

```
from openai import OpenAI# Point to local Ollama serverclient = instructor.from_openai(    OpenAI(        base_url="http://localhost:11434/v1",        api_key="ollama"# Required but ignored    mode=instructor.Mode.JSONresponse = client.chat.completions.create(    model="llama3.1",    response_model=YourModel,    messages=[...]
```

## Common Patterns[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#common-patterns "Direct link to Common Patterns")
### Pattern 1: Data Extraction from Text[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-1-data-extraction-from-text "Direct link to Pattern 1: Data Extraction from Text")

```
classCompanyInfo(BaseModel):    name:str    founded_year:int    industry:str    employees:int    headquarters:strtext ="""Tesla, Inc. was founded in 2003. It operates in the automotive and energyindustry with approximately 140,000 employees. The company is headquarteredin Austin, Texas."""company = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":f"Extract company information from: {text}"}],    response_model=CompanyInfo
```

### Pattern 2: Classification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-2-classification "Direct link to Pattern 2: Classification")

```
classCategory(str, Enum):    TECHNOLOGY ="technology"    FINANCE ="finance"    HEALTHCARE ="healthcare"    EDUCATION ="education"    OTHER ="other"classArticleClassification(BaseModel):    category: Category    confidence:float= Field(ge=0.0, le=1.0)    keywords:list[str]classification = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":"Classify this article: [article text]"}],    response_model=ArticleClassification
```

### Pattern 3: Multi-Entity Extraction[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-3-multi-entity-extraction "Direct link to Pattern 3: Multi-Entity Extraction")

```
classPerson(BaseModel):    name:str    role:strclassOrganization(BaseModel):    name:str    industry:strclassEntities(BaseModel):    people:list[Person]    organizations:list[Organization]    locations:list[str]text ="Tim Cook, CEO of Apple, announced at the event in Cupertino..."entities = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":f"Extract all entities from: {text}"}],    response_model=Entitiesfor person in entities.people:print(f"{person.name} - {person.role}")
```

### Pattern 4: Structured Analysis[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-4-structured-analysis "Direct link to Pattern 4: Structured Analysis")

```
classSentimentAnalysis(BaseModel):    overall_sentiment: Sentiment    positive_aspects:list[str]    negative_aspects:list[str]    suggestions:list[str]    score:float= Field(ge=-1.0, le=1.0)review ="The product works well but setup was confusing..."analysis = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[{"role":"user","content":f"Analyze this review: {review}"}],    response_model=SentimentAnalysis
```

### Pattern 5: Batch Processing[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-5-batch-processing "Direct link to Pattern 5: Batch Processing")

```
defextract_person(text:str)-> Person:return client.messages.create(        model="claude-sonnet-4-5-20250929",        max_tokens=1024,        messages=[{"role":"user","content":f"Extract person from: {text}"}],        response_model=Persontexts =["John Doe is a 30-year-old engineer","Jane Smith, 25, works in marketing","Bob Johnson, age 40, software developer"people =[extract_person(text)for text in texts]
```

## Advanced Features[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#advanced-features "Direct link to Advanced Features")
### Union Types[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#union-types "Direct link to Union Types")

```
from typing import UnionclassTextContent(BaseModel):type:str="text"    content:strclassImageContent(BaseModel):type:str="image"    url: HttpUrl    caption:strclassPost(BaseModel):    title:str    content: Union[TextContent, ImageContent]# Either type# LLM chooses appropriate type based on content
```

### Dynamic Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#dynamic-models "Direct link to Dynamic Models")

```
from pydantic import create_model# Create model at runtimeDynamicUser = create_model('User',    name=(str,...),    age=(int, Field(ge=0)),    email=(EmailStr,...)user = client.messages.create(    model="claude-sonnet-4-5-20250929",    max_tokens=1024,    messages=[...],    response_model=DynamicUser
```

### Custom Modes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#custom-modes "Direct link to Custom Modes")

```
# For providers without native structured outputsclient = instructor.from_anthropic(    Anthropic(),    mode=instructor.Mode.JSON  # JSON mode# Available modes:# - Mode.ANTHROPIC_TOOLS (recommended for Claude)# - Mode.JSON (fallback)# - Mode.TOOLS (OpenAI tools)
```

### Context Management[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#context-management "Direct link to Context Management")

```
# Single-use clientwith instructor.from_anthropic(Anthropic())as client:    result = client.messages.create(        model="claude-sonnet-4-5-20250929",        max_tokens=1024,        messages=[...],        response_model=YourModel# Client closed automatically
```

## Error Handling[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#error-handling "Direct link to Error Handling")
### Handling Validation Errors[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#handling-validation-errors "Direct link to Handling Validation Errors")

```
from pydantic import ValidationErrortry:    user = client.messages.create(        model="claude-sonnet-4-5-20250929",        max_tokens=1024,        messages=[...],        response_model=User,        max_retries=3except ValidationError as e:print(f"Failed after retries: {e}")# Handle gracefullyexcept Exception as e:print(f"API error: {e}")
```

### Custom Error Messages[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#custom-error-messages "Direct link to Custom Error Messages")

```
classValidatedUser(BaseModel):    name:str= Field(description="Full name, 2-100 characters")    age:int= Field(description="Age between 0 and 120", ge=0, le=120)    email: EmailStr = Field(description="Valid email address")classConfig:# Custom error messages        json_schema_extra ={"examples":["name":"John Doe","age":30,"email":"john@example.com"
```

## Best Practices[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#best-practices "Direct link to Best Practices")
### 1. Clear Field Descriptions[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#1-clear-field-descriptions "Direct link to 1. Clear Field Descriptions")

```
# ❌ Bad: VagueclassProduct(BaseModel):    name:str    price:float# ✅ Good: DescriptiveclassProduct(BaseModel):    name:str= Field(description="Product name from the text")    price:float= Field(description="Price in USD, without currency symbol")
```

### 2. Use Appropriate Validation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#2-use-appropriate-validation "Direct link to 2. Use Appropriate Validation")

```
# ✅ Good: Constrain valuesclassRating(BaseModel):    score:int= Field(ge=1, le=5, description="Rating from 1 to 5 stars")    review:str= Field(min_length=10, description="Review text, at least 10 chars")
```

### 3. Provide Examples in Prompts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#3-provide-examples-in-prompts "Direct link to 3. Provide Examples in Prompts")

```
messages =[{"role":"user","content":"""Extract person info from: "John, 30, engineer"Example format:  "name": "John Doe",  "age": 30,  "occupation": "engineer"}"""
```

### 4. Use Enums for Fixed Categories[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#4-use-enums-for-fixed-categories "Direct link to 4. Use Enums for Fixed Categories")

```
# ✅ Good: Enum ensures valid valuesclassStatus(str, Enum):    PENDING ="pending"    APPROVED ="approved"    REJECTED ="rejected"classApplication(BaseModel):    status: Status  # LLM must choose from enum
```

### 5. Handle Missing Data Gracefully[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#5-handle-missing-data-gracefully "Direct link to 5. Handle Missing Data Gracefully")

```
classPartialData(BaseModel):    required_field:str    optional_field: Optional[str]=None    default_field:str="default_value"# LLM only needs to provide required_field
```

## Comparison to Alternatives[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#comparison-to-alternatives "Direct link to Comparison to Alternatives")  
| Feature  | Instructor  | Manual JSON  | LangChain  | DSPy  |  
| --- | --- | --- | --- | --- |  
| Type Safety  | ✅ Yes  | ❌ No  | ⚠️ Partial  | ✅ Yes  |  
| Auto Validation  | ✅ Yes  | ❌ No  | ❌ No  | ⚠️ Limited  |  
| Auto Retry  | ✅ Yes  | ❌ No  | ❌ No  | ✅ Yes  |  
| Streaming  | ✅ Yes  | ❌ No  | ✅ Yes  | ❌ No  |  
| Multi-Provider  | ✅ Yes  | ⚠️ Manual  | ✅ Yes  | ✅ Yes  |  
| Learning Curve  | Low  | Low  | Medium  | High  |  
**When to choose Instructor:**
  * Need structured, validated outputs
  * Want type safety and IDE support
  * Require automatic retries
  * Building data extraction systems


**When to choose alternatives:**
  * DSPy: Need prompt optimization
  * LangChain: Building complex chains
  * Manual: Simple, one-off extractions


## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#resources "Direct link to Resources")
  * **Documentation** : <https://python.useinstructor.com>
  * **GitHub** : <https://github.com/jxnl/instructor> (15k+ stars)
  * **Cookbook** : <https://python.useinstructor.com/examples>
  * **Discord** : Community support available


## See Also[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#see-also "Direct link to See Also")
  * `references/validation.md` - Advanced validation patterns
  * `references/providers.md` - Provider-specific configuration
  * `references/examples.md` - Real-world use cases


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#reference-full-skillmd)
  * [When to Use This Skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#when-to-use-this-skill)
  * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#installation)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#quick-start)
    * [Basic Example: Extract User Data](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#basic-example-extract-user-data)
    * [With OpenAI](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#with-openai)
  * [Core Concepts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#core-concepts)
    * [1. Response Models (Pydantic)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#1-response-models-pydantic)
    * [2. Validation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#2-validation)
    * [3. Automatic Retrying](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#3-automatic-retrying)
    * [4. Streaming](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#4-streaming)
  * [Provider Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#provider-configuration)
    * [Anthropic Claude](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#anthropic-claude)
    * [Local Models (Ollama)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#local-models-ollama)
  * [Common Patterns](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#common-patterns)
    * [Pattern 1: Data Extraction from Text](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-1-data-extraction-from-text)
    * [Pattern 2: Classification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-2-classification)
    * [Pattern 3: Multi-Entity Extraction](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-3-multi-entity-extraction)
    * [Pattern 4: Structured Analysis](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-4-structured-analysis)
    * [Pattern 5: Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#pattern-5-batch-processing)
  * [Advanced Features](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#advanced-features)
    * [Union Types](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#union-types)
    * [Dynamic Models](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#dynamic-models)
    * [Custom Modes](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#custom-modes)
    * [Context Management](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#context-management)
  * [Error Handling](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#error-handling)
    * [Handling Validation Errors](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#handling-validation-errors)
    * [Custom Error Messages](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#custom-error-messages)
  * [Best Practices](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#best-practices)
    * [1. Clear Field Descriptions](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#1-clear-field-descriptions)
    * [2. Use Appropriate Validation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#2-use-appropriate-validation)
    * [3. Provide Examples in Prompts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#3-provide-examples-in-prompts)
    * [4. Use Enums for Fixed Categories](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#4-use-enums-for-fixed-categories)
    * [5. Handle Missing Data Gracefully](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#5-handle-missing-data-gracefully)
  * [Comparison to Alternatives](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-instructor#comparison-to-alternatives)


