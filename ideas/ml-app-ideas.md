# Mobile app ideas for practising deep learning

Finance / crypto / games, built from the Hugging Face task catalog.
Compiled 2026-10-13. Every model and dataset below was checked against the Hub API; sizes are
`safetensors` parameter totals where the Hub reports them. Anything I could not verify says so.

---

## 1. The task catalog, as it stands

From [huggingface.co/tasks](https://huggingface.co/tasks), grouped as the site groups them.

### Natural Language Processing
[Feature Extraction](https://huggingface.co/tasks/feature-extraction) ·
[Fill-Mask](https://huggingface.co/tasks/fill-mask) ·
[Question Answering](https://huggingface.co/tasks/question-answering) ·
[Sentence Similarity](https://huggingface.co/tasks/sentence-similarity) ·
[Summarization](https://huggingface.co/tasks/summarization) ·
[Table Question Answering](https://huggingface.co/tasks/table-question-answering) ·
[Text Classification](https://huggingface.co/tasks/text-classification) ·
[Text Generation](https://huggingface.co/tasks/text-generation) ·
**[Text Ranking](https://huggingface.co/tasks/text-ranking)** ·
[Token Classification](https://huggingface.co/tasks/token-classification) ·
[Translation](https://huggingface.co/tasks/translation) ·
[Zero-Shot Classification](https://huggingface.co/tasks/zero-shot-classification)

### Computer Vision
[Depth Estimation](https://huggingface.co/tasks/depth-estimation) ·
[Image Classification](https://huggingface.co/tasks/image-classification) ·
[Image Feature Extraction](https://huggingface.co/tasks/image-feature-extraction) ·
[Image Segmentation](https://huggingface.co/tasks/image-segmentation) ·
[Image-to-Image](https://huggingface.co/tasks/image-to-image) ·
[Image-to-Text](https://huggingface.co/tasks/image-to-text) ·
[Image-to-Video](https://huggingface.co/tasks/image-to-video) ·
**[Keypoint Detection](https://huggingface.co/tasks/keypoint-detection)** ·
[Mask Generation](https://huggingface.co/tasks/mask-generation) ·
[Object Detection](https://huggingface.co/tasks/object-detection) ·
[Video Classification](https://huggingface.co/tasks/video-classification) ·
[Text-to-Image](https://huggingface.co/tasks/text-to-image) ·
[Text-to-Video](https://huggingface.co/tasks/text-to-video) ·
[Unconditional Image Generation](https://huggingface.co/tasks/unconditional-image-generation) ·
[Video-to-Video](https://huggingface.co/tasks/video-to-video) ·
[Zero-Shot Image Classification](https://huggingface.co/tasks/zero-shot-image-classification) ·
[Zero-Shot Object Detection](https://huggingface.co/tasks/zero-shot-object-detection) ·
**[Text-to-3D](https://huggingface.co/tasks/text-to-3d)** · **[Image-to-3D](https://huggingface.co/tasks/image-to-3d)**

### Audio
[Audio Classification](https://huggingface.co/tasks/audio-classification) ·
[Audio-to-Audio](https://huggingface.co/tasks/audio-to-audio) ·
[Automatic Speech Recognition](https://huggingface.co/tasks/automatic-speech-recognition) ·
[Text-to-Speech](https://huggingface.co/tasks/text-to-speech)

### Tabular
[Tabular Classification](https://huggingface.co/tasks/tabular-classification) ·
[Tabular Regression](https://huggingface.co/tasks/tabular-regression)

### Multimodal
**[Any-to-Any](https://huggingface.co/models?pipeline_tag=any-to-any)** ·
[Audio-Text-to-Text](https://huggingface.co/tasks/audio-text-to-text) ·
[Document Question Answering](https://huggingface.co/tasks/document-question-answering) ·
**[Visual Document Retrieval](https://huggingface.co/tasks/visual-document-retrieval)** ·
[Image-Text-to-Text](https://huggingface.co/tasks/image-text-to-text) ·
**Image-Text-to-Image** · **Image-Text-to-Video** ·
[Video-Text-to-Text](https://huggingface.co/tasks/video-text-to-text) ·
[Visual Question Answering](https://huggingface.co/tasks/visual-question-answering)

### Reinforcement Learning
[Reinforcement Learning](https://huggingface.co/tasks/reinforcement-learning)

### New or unusual, worth knowing about
- **Text-to-3D (~140 models) and Image-to-3D (~783)** are the thinnest categories on the
  site — early enough that a working mobile pipeline would be unusual.
- **Any-to-Any (~11,700 models)** is now one of the largest tags, and is where the
  omni-modal models land. It is a grab-bag rather than a well-defined task.
- **Visual Document Retrieval** is the ColPali-style idea of embedding page *images* instead
  of extracted text. Directly useful for anything that ingests statements or filings.
- **Text Ranking** (rerankers) is listed as a first-class task now, not folded into
  sentence similarity.
- **Keypoint Detection** is a separate task from pose estimation libraries.
- **Time-series forecasting is not on the `/tasks` page at all**, but
  [`?pipeline_tag=time-series-forecasting`](https://huggingface.co/models?pipeline_tag=time-series-forecasting)
  is a live model filter with Chronos, TimesFM and Granite TTM under it. Worth knowing the
  catalog page and the model filters do not fully agree.
- **Graph neural networks have no task tag.** For the wallet-scam idea on your list you are
  on PyTorch Geometric / DGL, not the Hub.

---

## 2. Why these eight

Your existing list already covers time-series forecasting (Chronos/TimesFM), VLM document
scanning, Whisper voice logging, RL market-making, LLM negotiation, object detection on a poker
table, and GNNs for wallet risk. So these deliberately use the task families you have **not**
touched: audio classification, sentence similarity and ranking, video classification,
summarization, mask generation, keypoint detection, zero-shot detection, and tabular
inference — plus one RL idea that is a different game from market-making.

---

## 3. The ideas

### 3.1 VoiceGuard — live scam-call screener

**What the user does.** Starts VoiceGuard when an unknown caller claims to be from their bank
or exchange. The app streams the call audio through two models at once: one asks *is this voice
synthetic?*, the other transcribes and asks *is this a known scam script?* A bar fills as
evidence accumulates, and the app surfaces the specific phrases that triggered it — "remote
access", "transfer to a safe account", "read me the seed phrase".

**Tasks.** [Audio Classification](https://huggingface.co/tasks/audio-classification) ·
[Automatic Speech Recognition](https://huggingface.co/tasks/automatic-speech-recognition) ·
[Text Classification](https://huggingface.co/tasks/text-classification)

**Models.**
| model | size | license |
|---|---|---|
| [`MelodyMachine/Deepfake-audio-detection-V2`](https://huggingface.co/MelodyMachine/Deepfake-audio-detection-V2) | 95M | apache-2.0 |
| [`WpythonW/ast-fakeaudio-detector`](https://huggingface.co/WpythonW/ast-fakeaudio-detector) | 86M | apache-2.0 |
| [`openai/whisper-small`](https://huggingface.co/openai/whisper-small) | 242M | apache-2.0 |

**Data.** [`SpeechAntiSpoofingBenchmarks/ASVspoof2019_LA`](https://huggingface.co/datasets/SpeechAntiSpoofingBenchmarks/ASVspoof2019_LA)
and [`ASVspoof2021_DF`](https://huggingface.co/datasets/SpeechAntiSpoofingBenchmarks/ASVspoof2021_DF)
are the standard anti-spoofing corpora and both have real download traffic.
[`garystafford/deepfake-audio-detection`](https://huggingface.co/datasets/garystafford/deepfake-audio-detection)
is a smaller convenience set. The scam-script classifier you build yourself: scrape published
警察庁 / FCA / FTC scam transcripts, then synthesise variants with a small LLM — a legitimate
use of generation for data augmentation.

**On-device.** Yes for the spoof detector — a 95M audio classifier quantises to well under
100 MB. Whisper runs on-device via Core ML (whisper.cpp) or ONNX Runtime Mobile; start from
[`onnx-community/whisper-tiny.en`](https://huggingface.co/onnx-community/whisper-tiny.en) and
move up. This app *must* be on-device: streaming call audio to a server is the wrong design
for a privacy-sensitive fraud tool.

**Skills.** Fine-tuning an audio spectrogram transformer; streaming/windowed inference with
hysteresis so the score does not flicker; **calibration** — this is a false-positive-sensitive
classifier and accusing a real bank is the costly error; int8 quantization; running two models
concurrently under a latency budget.

**Difficulty 4/5.** **Weekend one.** Drop the live-call part entirely. Record ten fake and ten
real voice clips, fine-tune the AST spoof detector on ASVspoof, and build a screen that plays a
clip and shows a score. Live audio capture is the hard half — defer it.

---

### 3.2 Déjà Vu — token whitepaper plagiarism detector

**What the user does.** Pastes a URL or PDF for a token they are considering. The app embeds it
section by section, compares against a local index of known rug-pull and template whitepapers,
and returns nearest neighbours with the matching passages highlighted side by side — "this
tokenomics section is 0.94 cosine to three 2021 rugs."

**Tasks.** [Sentence Similarity](https://huggingface.co/tasks/sentence-similarity) ·
[Text Ranking](https://huggingface.co/tasks/text-ranking) ·
[Zero-Shot Classification](https://huggingface.co/tasks/zero-shot-classification)

**Models.**
| model | size | license |
|---|---|---|
| [`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | ~22M | apache-2.0 |
| [`BAAI/bge-small-en-v1.5`](https://huggingface.co/BAAI/bge-small-en-v1.5) | 33M | mit |
| [`MoritzLaurer/deberta-v3-base-zeroshot-v2.0`](https://huggingface.co/MoritzLaurer/deberta-v3-base-zeroshot-v2.0) | 184M | mit |

**Data.** No whitepaper corpus exists on the Hub — I searched and found nothing usable. You
build it: scrape whitepapers for tokens flagged on rug-pull trackers, plus a control set of
surviving projects. A few hundred documents is enough for retrieval; labelling is
coarse (`rugged` / `alive`) and comes free from the tracker.

**On-device.** Entirely. A 22M embedding model runs fine via
[`Xenova/all-MiniLM-L6-v2`](https://huggingface.co/Xenova/all-MiniLM-L6-v2) (ONNX) or a Core ML
export, and the index is a few megabytes of float16. The zero-shot DeBERTa is better kept
server-side or swapped for a fine-tuned small classifier.

**Skills.** Embedding models and vector search; **contrastive fine-tuning** with
`MultipleNegativesRankingLoss` to pull template clones together; two-stage retrieval
(bi-encoder recall, cross-encoder rerank); honest evaluation of a retrieval system — recall@k
rather than accuracy.

**Difficulty 2/5.** **Weekend one.** 50 whitepapers, MiniLM embeddings, `faiss` or plain numpy
cosine, one screen showing the top-5 neighbours with matched paragraphs. No fine-tuning yet.

---

### 3.3 Grade It — trading-card condition grader

**What the user does.** Lays a card on a table, and the app guides them to a square-on shot.
It identifies the card, then measures what graders measure: **centering** (border widths from
segmentation masks), **corners and edges** (crops classified for wear), and **surface**
(scratches and print lines, with a depth map as a side channel). Output is a predicted grade
with a per-criterion breakdown and the measurements behind it.

**Tasks.** [Mask Generation](https://huggingface.co/tasks/mask-generation) ·
[Image Segmentation](https://huggingface.co/tasks/image-segmentation) ·
[Keypoint Detection](https://huggingface.co/tasks/keypoint-detection) ·
[Image Classification](https://huggingface.co/tasks/image-classification) ·
[Zero-Shot Image Classification](https://huggingface.co/tasks/zero-shot-image-classification) ·
[Depth Estimation](https://huggingface.co/tasks/depth-estimation)

**Models.**
| model | size | license |
|---|---|---|
| [`facebook/sam-vit-base`](https://huggingface.co/facebook/sam-vit-base) | 94M | apache-2.0 |
| [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224) (fine-tune for corner wear) | 86M | apache-2.0 |
| [`openai/clip-vit-base-patch32`](https://huggingface.co/openai/clip-vit-base-patch32) (zero-shot card ID) | ~151M | license not stated on the card |
| [`depth-anything/Depth-Anything-V2-Small-hf`](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf) | 25M | apache-2.0 |

**Data.** **There is no card-grading dataset on the Hub** — I searched `card grading` and got
nothing. Card *images* exist in small community sets such as
[`netprtony/pokemon-cards-image-and-annotations`](https://huggingface.co/datasets/netprtony/pokemon-cards-image-and-annotations)
and [`tooni/pokemoncards`](https://huggingface.co/datasets/tooni/pokemoncards), but none carry
condition labels. You create the data, and that is the interesting part: photograph your own
cards, and get labels free by scraping completed listings of **already-graded** slabs, where
the grade is printed on the label. That is a genuinely clever weak-supervision setup.

**On-device.** Mostly. SAM-base is borderline but there are mobile SAM variants; Depth-Anything-V2-Small
has a verified Core ML export at
[`apple/coreml-depth-anything-small`](https://huggingface.co/apple/coreml-depth-anything-small)
and an ONNX one at [`onnx-community/depth-anything-v2-small`](https://huggingface.co/onnx-community/depth-anything-v2-small).
The classifier heads are tiny.

**Skills.** Multi-head / multi-task learning (four criteria, one backbone); turning a
segmentation mask into a **geometric measurement** rather than a label, which is a different
discipline from classification; **ordinal regression** — grades 1–10 are ordered, so treating
them as unordered classes throws away structure; capture-quality gating, because a bad photo
should be rejected rather than scored.

**Difficulty 4/5.** **Weekend one.** Centering only. SAM to mask the card and the inner border,
compute left/right and top/bottom border ratios, show the numbers. No grade prediction, no
learning — just the measurement, which is already useful and proves the capture pipeline.

---

### 3.4 Pull Audit — gacha odds auditor

**What the user does.** Photographs a game's published drop-rate table; a VLM parses it into
structured rates. Then they log pulls — or screenshot the results and let the model read them.
The app maintains a **Bayesian posterior** over the true rate and tells them when their
observed pulls are genuinely inconsistent with the disclosure, with a sequential test that
does not lie about multiple looks at the data.

**Tasks.** [Document Question Answering](https://huggingface.co/tasks/document-question-answering) ·
[Image-Text-to-Text](https://huggingface.co/tasks/image-text-to-text) ·
[Table Question Answering](https://huggingface.co/tasks/table-question-answering) ·
[Tabular Classification](https://huggingface.co/tasks/tabular-classification)

**Models.**
| model | size | license |
|---|---|---|
| [`HuggingFaceTB/SmolVLM-256M-Instruct`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct) | 256M | apache-2.0 |
| [`Qwen/Qwen2.5-VL-3B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) | 3.75B | license not stated on the card — check before shipping |
| [`impira/layoutlm-document-qa`](https://huggingface.co/impira/layoutlm-document-qa) | ~128M | mit |
| [`microsoft/tapex-base-finetuned-wtq`](https://huggingface.co/microsoft/tapex-base-finetuned-wtq) | 139M | mit |

**Data.** Your own, and it is easy: screenshot real gacha rate tables (they are published
because JOGA/CESA guidelines require it) and hand-label fifty into JSON. For the statistical
side you need no data at all — you simulate pulls with pity timers and ceilings and check your
test's false-positive rate against ground truth you control.

**On-device.** SmolVLM-256M is genuinely phone-sized; Qwen2.5-VL-3B needs a server or a
high-end device with aggressive quantization. The statistics are arithmetic.

**Skills.** Structured extraction from a VLM — constrained decoding into JSON, which is a real
skill and badly underrated; evaluating extraction (field-level accuracy, not BLEU); and the
honest statistics of **sequential testing**, where the fun is proving to yourself that "I did
80 pulls and got nothing, the rates must be fake" is usually not significant.

**Difficulty 3/5.** **Weekend one.** Skip the camera. Type in a rate and your pull results, and
show the posterior with a credible interval and a sequential-test verdict. The hard,
interesting part is the statistics, and it needs no ML to start.

---

### 3.5 Tell — gameplay cheat spotter

**What the user does.** Shares a suspicious clip from a match. The app classifies short windows
of the video for inhuman aim behaviour — snap-to-target, zero overshoot, inhuman reaction
latency — and returns a timeline of flagged moments with the motion traces drawn over the
frames, rather than a bare verdict.

**Tasks.** [Video Classification](https://huggingface.co/tasks/video-classification) ·
[Keypoint Detection](https://huggingface.co/tasks/keypoint-detection) ·
[Object Detection](https://huggingface.co/tasks/object-detection)

**Models.**
| model | size | license |
|---|---|---|
| [`MCG-NJU/videomae-base-finetuned-kinetics`](https://huggingface.co/MCG-NJU/videomae-base-finetuned-kinetics) | 87M | cc-by-nc-4.0 (non-commercial) |
| [`facebook/timesformer-base-finetuned-k400`](https://huggingface.co/facebook/timesformer-base-finetuned-k400) | not reported by the API | cc-by-nc-4.0 |
| [`hustvl/yolos-tiny`](https://huggingface.co/hustvl/yolos-tiny) (crosshair / target tracking) | 6M | apache-2.0 |

**Data.** Yours, and you can generate the positives: play a game with a *legitimate* assist
setting cranked up, or script mouse input to produce synthetic aimbot traces, against your own
normal play as negatives. [`taesiri/GameplayVideoSplits`](https://huggingface.co/datasets/taesiri/GameplayVideoSplits)
exists but is tiny. **Note the licences** — both video backbones are non-commercial, which is
fine for practice and not for shipping.

**On-device.** Server, realistically. Video transformers over a clip are not a phone workload;
the phone records and uploads, the server scores. A tracking-only version with YOLOS-tiny could
run locally.

**Skills.** Temporal modelling and clip sampling; **the derivative trick** — the signal is not
in the pixels but in the *trajectory* of the crosshair, so extracting motion first and
classifying that is both cheaper and more accurate than a video transformer; extreme class
imbalance; and adversarial thinking, since cheats now deliberately add human-like jitter.

**Difficulty 4/5.** **Weekend one.** No video model. Track the crosshair with YOLOS-tiny,
extract angular velocity and acceleration, and plot your own aim traces next to a scripted
snap. If those two are visually separable, the whole project is viable; if not, you have saved
yourself weeks.

---

### 3.6 Proposal Pulse — DAO governance reader and vote predictor

**What the user does.** Opens the app to a feed of live governance proposals across the DAOs
they hold tokens in. Each gets a three-line summary, a classification of what it actually does
(treasury spend / parameter change / upgrade / social), a flag for anything that touches their
position, and a **predicted outcome** based on how the large delegates have voted historically.

**Tasks.** [Summarization](https://huggingface.co/tasks/summarization) ·
[Zero-Shot Classification](https://huggingface.co/tasks/zero-shot-classification) ·
[Token Classification](https://huggingface.co/tasks/token-classification) ·
[Tabular Classification](https://huggingface.co/tasks/tabular-classification)

**Models.**
| model | size | license |
|---|---|---|
| [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn) | 406M | mit |
| [`sshleifer/distilbart-cnn-12-6`](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | not reported by the API | apache-2.0 |
| [`facebook/bart-large-mnli`](https://huggingface.co/facebook/bart-large-mnli) | 407M | mit |
| [`Qwen/Qwen2.5-0.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) (fine-tune for on-device summarising) | 494M | apache-2.0 |

**Data.** No usable governance corpus on the Hub — the only hit was
[`achiepatricia/han-governance-proposal-dataset-v1`](https://huggingface.co/datasets/achiepatricia/han-governance-proposal-dataset-v1)
with 17 downloads, which is not a dataset you build on. Pull it yourself from the Snapshot and
Tally public APIs: proposal text, choices, final tallies, and per-delegate votes. **The labels
are free and already in the data** — outcomes are recorded — which makes this one of the
cleanest supervised setups on this list.

**On-device.** The vote predictor is a small tabular model and runs anywhere. Summarization
with BART-large needs a server; a LoRA-tuned Qwen2.5-0.5B would be the on-device route and is a
good exercise in itself.

**Skills.** **LoRA / PEFT** fine-tuning for domain summarization, which is the single most
transferable skill on this list; measuring summarization honestly (humans or an LLM judge, not
ROUGE alone); combining a text model with a tabular one; and the forecasting discipline you
already like — a vote predictor is a calibrated binary forecaster and deserves a Brier score.

**Difficulty 3/5.** **Weekend one.** Vote prediction only, no NLP. Pull 500 closed Snapshot
proposals, features = top-10 delegate voting history plus quorum and proposal type, fit
gradient boosting, and report the Brier score against the base rate. That tells you whether
governance is predictable before you spend time on summaries.

---

### 3.7 Last Look — RL auction trainer

**What the user does.** Bids against trained agents in a sequence of auctions — NFT drops,
collectible lots, liquidation auctions — with the format switching between English, sealed-bid
and Dutch. Afterwards the app decomposes the loss: how much came from the winner's curse, how
much from bidding against a thin book, how much from simply overpaying. Agents are visibly
labelled by policy so the user learns which behaviour beat them.

**Tasks.** [Reinforcement Learning](https://huggingface.co/tasks/reinforcement-learning)

**Models.** Nothing off-the-shelf fits — auction environments are not a standard Hub benchmark,
and I will not pretend otherwise. You train your own with
[Stable-Baselines3](https://huggingface.co/sb3) as the reference implementation;
[`sb3/ppo-LunarLander-v2`](https://huggingface.co/sb3/ppo-LunarLander-v2) exists and is useful
only as a template for how to package and upload a trained policy to the Hub.

**Data.** None needed — the environment *is* the data, which is the appeal. Write a Gymnasium
env with configurable private-value distributions and bidder counts. Optionally calibrate the
value distribution to real OpenSea or Blur sale histories so the game feels like the market
rather than a textbook.

**On-device.** Entirely. A trained PPO policy for a low-dimensional auction is tiny — tens of
kilobytes — and runs as an ONNX or Core ML model with no server at all.

**Skills.** The full RL loop: environment design (the hard part, and the part tutorials skip),
reward shaping, PPO, self-play, and the thing that makes this finance rather than games —
checking your agent against the **known analytic equilibrium**. First-price sealed-bid auctions
with uniform private values have a closed-form optimal bid, so you can verify your agent
actually converged instead of merely looking busy. That is a rare luxury in RL.

**Difficulty 3/5.** **Weekend one.** One format, second-price sealed bid, three bidders, uniform
values. Train PPO, then plot the learned bid function against the analytic one. If they
coincide, the scaffolding works.

---

### 3.8 Level Up — photo to playable level

**What the user does.** Photographs anything — a desk, a street, a bookshelf. The app segments
it into solid regions, turns the masks into collision geometry, and drops a character in. The
user plays a platformer built out of their own surroundings, then shares the level as a photo
plus a seed.

**Tasks.** [Mask Generation](https://huggingface.co/tasks/mask-generation) ·
[Image Segmentation](https://huggingface.co/tasks/image-segmentation) ·
[Depth Estimation](https://huggingface.co/tasks/depth-estimation) ·
[Zero-Shot Object Detection](https://huggingface.co/tasks/zero-shot-object-detection)

**Models.**
| model | size | license |
|---|---|---|
| [`facebook/sam-vit-base`](https://huggingface.co/facebook/sam-vit-base) | 94M | apache-2.0 |
| [`depth-anything/Depth-Anything-V2-Small-hf`](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf) | 25M | apache-2.0 |
| [`IDEA-Research/grounding-dino-tiny`](https://huggingface.co/IDEA-Research/grounding-dino-tiny) (label regions by text: "water", "spikes") | ~172M | apache-2.0 |

**Data.** None. Every model here is used zero-shot — which is the point, and makes this the
lowest-friction project on the list.

**On-device.** Yes, and this one should be: verified Core ML
([`apple/coreml-depth-anything-small`](https://huggingface.co/apple/coreml-depth-anything-small))
and ONNX ([`onnx-community/depth-anything-v2-small`](https://huggingface.co/onnx-community/depth-anything-v2-small))
exports exist for depth, and SAM has mobile variants. Grounding DINO is the heaviest piece and
is optional.

**Skills.** Model *export and deployment* rather than training — Core ML / ONNX conversion,
quantization, measuring latency and memory on a real device, running two models in one frame
budget. Plus the engineering skill nobody teaches: converting a soft probabilistic mask into
hard geometry a physics engine will accept.

**Difficulty 2/5.** **Weekend one.** Still images only, no game. Tap a photo, SAM segments the
region, draw the mask outline as a polygon. If the polygons look like level geometry, continue;
if they look like noise, you have learned something cheap.

---

## 4. Top three

**1. Grade It (3.3).** The one I would build first, because the *data* is the exercise. Getting
labels by scraping already-graded slabs is a weak-supervision trick you will reuse for the rest
of your career, and the problem forces three things finance people are usually weak at:
measurement from masks rather than classification, ordinal targets, and input-quality gating.
It also has a real market — graded-card pricing is a liquid asset class with public comps, so
your model output has a verifiable dollar value. That closes the loop in a way a game does not.

**2. VoiceGuard (3.1).** The hardest and the most worth doing. It is genuinely useful, it has to
be on-device for reasons you can articulate, and it is the only idea here where **calibration is
the whole product** — a scam detector that cries wolf gets uninstalled. That is the same
discipline as the model-risk work: the cost of a false positive and a false negative are
different and you must say so explicitly. It also combines three modalities under a latency
budget, which is the most realistic engineering any of these will give you.

**3. Last Look (3.7).** Pick this third precisely because it is the one with no dataset and no
pretrained model — you build the environment, train the agent, and then **check it against a
closed-form answer**. Almost nothing in deep learning lets you verify convergence against known
truth, and an auction game does. Given your background it will also teach you something real
about bidding, which the deep-hedging game on your list will not: hedging is about variance,
auctions are about adverse selection.

**Honourable mention: Déjà Vu (3.2)** is the easiest thing here and the fastest route to
something you would actually show someone. If you want a win this weekend rather than a
project, start there.

---

## 5. Caveats

- **Download counts and sizes** were read from the Hub API on 2026-10-13. Sizes come from
  `safetensors.total`; where the API did not report it I have said so rather than guessed.
- **Three licences need checking before you ship anything**: `Qwen/Qwen2.5-VL-3B-Instruct` and
  `openai/clip-vit-base-patch32` do not state a licence in their card metadata, and both video
  backbones in 3.5 are **cc-by-nc-4.0** — non-commercial.
- `ProsusAI/finbert` is **cc-by-nc-sa-4.0**, which is why it is not recommended above despite
  being the obvious finance sentiment model.
- **Datasets I could not find**, stated plainly: no card-grading corpus, no token-whitepaper
  corpus, no usable DAO-governance corpus, no aimbot corpus. In all four cases building the
  dataset is the most valuable part of the project.
