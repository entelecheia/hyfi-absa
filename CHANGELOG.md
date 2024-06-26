<!--next-version-placeholder-->

## v0.5.1 (2024-03-29)

### Fix

* **dependencies:** Upgrade hyfi version to ^1.36.3 ([`687d53a`](https://github.com/entelecheia/hyfi-absa/commit/687d53a4a7d9b48f2373d6c7cf5fcfa98602ac21))

## v0.5.0 (2023-09-09)

### Feature

* **pipeline:** Add convert_output in config ([`468fb18`](https://github.com/entelecheia/hyfi-absa/commit/468fb18cfd0420005b83dbad6dc2e2f0a0964a29))
* **hyabsa:** Add convert_absa_output_to_results in pipe and run configs ([`eef96b2`](https://github.com/entelecheia/hyfi-absa/commit/eef96b297c0de7688f2771414413729cef0a845c))
* **test_results:** Add HyFI.generate_pipe_config function call ([`e53c9db`](https://github.com/entelecheia/hyfi-absa/commit/e53c9dbcf3c061e1c4814cdee6cfe593d755af17))
* **tests:** Add new test_results module in hyabsa/agents tests ([`cbd9cce`](https://github.com/entelecheia/hyfi-absa/commit/cbd9ccef1d274c8dfef43b4fe621c50b3f83d073))
* **results:** Add convert_output_to_results function ([`0dfe260`](https://github.com/entelecheia/hyfi-absa/commit/0dfe260d1b1a7c512fd00c48db14f6dc9d044095))

## v0.4.1 (2023-09-07)

### Fix

* **openai:** Replace backoff with tenacity for retries ([`d266340`](https://github.com/entelecheia/hyfi-absa/commit/d266340ea4eb00664dab93a30f95e24f34cf3950))
* **dependencies:** Replace backoff with tenacity ([`f40b0ce`](https://github.com/entelecheia/hyfi-absa/commit/f40b0cebd7754c948c954621b4fde592f7d8ba87))

## v0.4.0 (2023-09-04)

### Feature

* **absa:** Add id column to batch_run and execute_each functions ([`8422d63`](https://github.com/entelecheia/hyfi-absa/commit/8422d63e66a4971f470f701f18bce9ee5c642c5d))
* **hyabsa:** Add id column and rename bodyText to text in absa config ([`f35f44f`](https://github.com/entelecheia/hyfi-absa/commit/f35f44fdfc356978c714dffafb896518e028f7bd))
* **AgentResult:** Add id field ([`65dd028`](https://github.com/entelecheia/hyfi-absa/commit/65dd0282bbac13fd607c919a217d2f1e659b7e10))
* **absa:** Add id parameter to execute method ([`10439ef`](https://github.com/entelecheia/hyfi-absa/commit/10439ef78a938db23ba9af56716fd7379fc21bb6))
* **runner:** Add id_col and text_col in test.yaml ([`4ca52bd`](https://github.com/entelecheia/hyfi-absa/commit/4ca52bd272fee8526dc84ec93937123cf4622e60))

## v0.3.3 (2023-08-25)

### Fix

* **openai:** Add ChatCompletionEnv class, refactor environment variables access ([`ced15cb`](https://github.com/entelecheia/hyfi-absa/commit/ced15cb79de5a0d403b2fffe444952804efa40b5))
* **dependencies:** Upgrade hyfi to 1.32.1 ([`5e16a32`](https://github.com/entelecheia/hyfi-absa/commit/5e16a326c201e392fa7a5589147a1775c982f0ff))

## v0.3.2 (2023-08-08)

### Fix

* **hyabsa:** Modify configuration in __init__.yaml files for agent, llm and prompts. ([`f5c55dd`](https://github.com/entelecheia/hyfi-absa/commit/f5c55dd2a1ce411f57da161c6ca0d3237124d5c4))
* **openai:** Replace dotenv with DotEnvConfig ([`263a0ce`](https://github.com/entelecheia/hyfi-absa/commit/263a0cedadceb1eafdb9df69463ea2eb89e60650))
* **runner:** Remove project from absa.yaml ([`16bb682`](https://github.com/entelecheia/hyfi-absa/commit/16bb682765401b9cf13af3dbe252ba9bb71028cb))
* **dependencies:** Upgrade hyfi to 1.25.0 ([`44730e4`](https://github.com/entelecheia/hyfi-absa/commit/44730e433ba82b528c129137b7f032f5cb4638e6))

## v0.3.1 (2023-08-04)

### Fix

* **pipeline:** Rename num_samples to sample_size in test.yaml ([`5b1022a`](https://github.com/entelecheia/hyfi-absa/commit/5b1022a8877b553fbfb874020b2f0c90b65d5859))

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
