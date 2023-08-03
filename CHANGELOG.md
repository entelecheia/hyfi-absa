<!--next-version-placeholder-->

## v0.3.0 (2023-08-03)

### Feature

* **openai:** Set API key and initialize ChatCompletion API ([`611ca18`](https://github.com/entelecheia/hyfi-absa/commit/611ca188415dd7db4b3c33adadfbab7aec1de330))
* **base agent:** Add timestamp to output_filename, add verbose parameter to execute function ([`c6a531d`](https://github.com/entelecheia/hyfi-absa/commit/c6a531d60eaa14ad5daa9c3286472e5c85cbc0f4))
* **config:** Add test-gpt4.yaml and gpt4.yaml configuration files, update absa.yaml with more configurations, create gpt4.yaml configuration file ([`257c6e6`](https://github.com/entelecheia/hyfi-absa/commit/257c6e62918e10eb05e1ef9e4637a07c3ecf49de))

### Fix

* **absa:** Add top_n attribute for row selection ([`1920f42`](https://github.com/entelecheia/hyfi-absa/commit/1920f42f8b5949f5d77ca496e28ce409ced579a9))

## v0.2.0 (2023-08-02)

### Feature

* **hyabsa/agents:** Add directory creation in base agent ([`796135f`](https://github.com/entelecheia/hyfi-absa/commit/796135f3cf602c5f2a1ccfd7d59363c3213b0e96))
* **runner:** Add train split to test configuration ([`3e502f5`](https://github.com/entelecheia/hyfi-absa/commit/3e502f5e36f43b6b62c6f2ff57c0e612b5a83d26))
* **agent:** Rename /api to /llm in __init__.yaml, add new absa.yaml with configurations ([`aa6d8b0`](https://github.com/entelecheia/hyfi-absa/commit/aa6d8b09d1985acabf363122411b39a22090b177))
* **tests:** Add basic tests for BaseAgent and AbsaRunner ([`0cb0f59`](https://github.com/entelecheia/hyfi-absa/commit/0cb0f59bd6802f2685bb4921032b0eb4391262bf))
* **runners:** Add AbsaRunner class and support methods in absa.py ([`b63df84`](https://github.com/entelecheia/hyfi-absa/commit/b63df8495958e8ba16f706c3fd5a2818f45f41f8))
* **prompts:** Add build function for generating prompts ([`408da56`](https://github.com/entelecheia/hyfi-absa/commit/408da56cffa0f64829cda21b6911837f1834cebd))
* **runners:** Add AbsaRunner to __init__ ([`f5147cf`](https://github.com/entelecheia/hyfi-absa/commit/f5147cf33e6b6d2a2542ec54d2ac30c8636cae47))
* **hyabsa-contexts:** Add ChatMessage model ([`659ddb5`](https://github.com/entelecheia/hyfi-absa/commit/659ddb51753aaa7ed574270a857bcdf0d091dd3c))
* **hyabsa:** Add AgentResult class in results.py ([`9048d35`](https://github.com/entelecheia/hyfi-absa/commit/9048d35bae7cf91c8dd5c03b3692d21ceedba9ea))
* **hyabsa/llms:** Add OpenAI ChatCompletion classes and methods ([`f42029b`](https://github.com/entelecheia/hyfi-absa/commit/f42029b273c4e51ac8830da5c217092f9dcae3e9))
* **hyabsa:** Add new class BaseAgent and associated methods ([`5df6656`](https://github.com/entelecheia/hyfi-absa/commit/5df6656a43e01b070de07aa8513a9d1427fe1b1a))
* **hyabsa:** Add AbsaAgent class and execute method ([`b9d3560`](https://github.com/entelecheia/hyfi-absa/commit/b9d3560f867a443325aebd66b8381593f2103f3f))
* **config:** Add test.yaml configuration file ([`caafad3`](https://github.com/entelecheia/hyfi-absa/commit/caafad3e8b1d50dc2fa6580e3a798044eaca02f3))
* **absa:** Add prediction functions for ABSA model ([`5197b9a`](https://github.com/entelecheia/hyfi-absa/commit/5197b9a258ae9ad50475e0ad7be97efc7680b908))
* **prompts:** Add new prompts module ([`4fc3a1e`](https://github.com/entelecheia/hyfi-absa/commit/4fc3a1e086e7fed09b927f84ba208de74f131186))
* **prompts:** Add initial and default configuration files ([`15f0e97`](https://github.com/entelecheia/hyfi-absa/commit/15f0e97d39346a67ee428a199f7da76a67b30645))
* **api:** Add configuration for openai, gpt35, and gpt4 models ([`163b97c`](https://github.com/entelecheia/hyfi-absa/commit/163b97c17508d4194e1e27c95079c8a6e419b2bd))
* **hyabsa/conf/agent:** Initialize AbsaAgent configs ([`ac2da0f`](https://github.com/entelecheia/hyfi-absa/commit/ac2da0f114967f1b398adeafa3691730a0f1115c))
* **openai-api:** Implement functionality to interact with OpenAI API ([`003ee0d`](https://github.com/entelecheia/hyfi-absa/commit/003ee0d570a42407b41a1f9313104aa66fff35b4))
* **hyabsa/api:** Add OpenaiAPI module ([`bc2a50b`](https://github.com/entelecheia/hyfi-absa/commit/bc2a50b2c3a437816d9fa2ea5eaac7e5aaa0d1f2))
* **hyabsa:** Add AbsaAgent class with generate_prompt and predict methods ([`e451a12`](https://github.com/entelecheia/hyfi-absa/commit/e451a12a246f7d344e4cee16f07db5d6820a162e))
* **config:** Add test configuration files for pipeline, project, task and workflow ([`2e50659`](https://github.com/entelecheia/hyfi-absa/commit/2e506598b25db4638a3b402e9e67ad910c284995))
* **tests:** Add sample_100.parquet data file ([`8ee7b27`](https://github.com/entelecheia/hyfi-absa/commit/8ee7b27394d8a1a7bd278753087462563328680e))
* **dependencies:** Upgrade hyfi to 1.14.0 and add backoff and openai dependencies ([`bcac9c0`](https://github.com/entelecheia/hyfi-absa/commit/bcac9c09a938b689b8ad6ea573938619b07747e9))

### Fix

* **absa:** Adjust task prediction and agent model handling ([`1fca422`](https://github.com/entelecheia/hyfi-absa/commit/1fca422b17586d77a67793202b082b36f1c78880))

## v0.1.0 (2023-07-30)

### Feature

* Initial version ([`0069ea5`](https://github.com/entelecheia/hyfi-absa/commit/0069ea5eac51add4d0809e1cdf0241f450a5457b))
