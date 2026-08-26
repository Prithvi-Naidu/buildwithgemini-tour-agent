<div align="center">

# 🏡 Airbnb TourCraft AI — 3D Spatial Video Tour Generator

[![Build with Gemini](https://img.shields.io/badge/Build%20with-Gemini%202.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Vertex AI Veo 3.1](https://img.shields.io/badge/Video%20Gen-Veo%203.1%20Image--to--Video-0F9D58?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/vertex-ai)
[![Google ADK Framework](https://img.shields.io/badge/Agent-Google%20ADK%20Framework-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://github.com/google/agent-development-kit)
[![Google Cloud TTS](https://img.shields.io/badge/Audio-Cloud%20Text--to--Speech-EA4335?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/text-to-speech)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.style=for-the-badge)](LICENSE)

<br/>

### 🎬 *Transforming static 2D listing photos into photorealistic, steadycam 3D spatial room walkthrough video tours with AI voiceover narration.*

<br/>

![3D Veo Walkthrough Demo](demo_preview.gif)

*3D Spatial Room Walkthrough Video generated directly from 2D photos using **Vertex AI Veo 3.1***

</div>

---

## 🍿 Live Video Tour Demos

### 🌟 Full 7-Room Stitched 3D Tour Package
> 🎬 **[Watch Full Property 3D AI Video Tour (1080p MP4)](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/full_property_3d_veo_tour.mp4)**

<br/>

### 🎥 Individual 3D AI Scene Video Clips

| Scene | Room Space | Veo 3.1 3D Video Clip |
| :---: | :--- | :--- |
| **01** | 🛋️ **Sunlit Living Room** | 🎬 **[Play Living Room 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/4465040356510722226/sample_0.mp4)** |
| **02** | 🍳 **Chef Kitchen** | 🎬 **[Play Kitchen 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/883659396315306320/sample_0.mp4)** |
| **03** | 🛏️ **Master Bedroom** | 🎬 **[Play Master Bedroom 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/4418851399995325039/sample_0.mp4)** |
| **04** | 🛁 **Full Spa Bathroom** | 🎬 **[Play Spa Bathroom 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/17338547557530660932/sample_0.mp4)** |
| **05** | 🌲 **Private Outdoor Deck** | 🎬 **[Play Outdoor Deck 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/4884678098165555434/sample_0.mp4)** |
| **06** | ♨️ **Private Hot Tub** | 🎬 **[Play Hot Tub 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/18295272265328801438/sample_0.mp4)** |
| **07** | 🌳 **Lush Forest Backyard** | 🎬 **[Play Backyard 3D Video](https://storage.googleapis.com/qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos/5466190193047210232/sample_0.mp4)** |

---

## ✨ Features & Capabilities

- **🧠 Gemini 2.5 Flash Scene Intelligence**: Sequences listing photos into a logical real estate flow and crafts customized 3D motion prompts.
- **🎬 Vertex AI Veo 3.1 (`veo-3.1-fast-generate-001`)**: Generates 3D spatial room depth, steadycam forward dolly motion, and volumetric lighting directly from 2D images.
- **🎙️ Google Cloud Text-to-Speech**: Synthesizes professional AI tour guide voiceover narration synchronized with room clips.
- **🎞️ Automated ffmpeg Video Stitcher**: Merges multi-room 3D video clips and voiceover narration into a single 1080p MP4 package.
- **☁️ Cloud Storage Publishing**: Directly uploads final tour packages to public Google Cloud Storage (`gs://qwiklabs-gcp-03-ae2ceb20cd60-public-tour-videos`).
- **💻 ADK Interactive Web UI**: Fully integrated with Google ADK for rich chat and video preview rendering.

---

## 🛠️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              User / Airbnb Listing Photos              │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            Gemini 2.5 Flash Vision Model                │
│    (Sequences scenes & writes 3D motion prompts)       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│        Vertex AI Veo 3.1 Image-to-Video Model           │
│    (Generates 3D spatial room walkthrough clips)        │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            Google Cloud Text-to-Speech                  │
│       (Synthesizes tour guide audio narration)          │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│             ffmpeg Video Assembly Pipeline              │
│       (Stitches 7 3D clips + voiceover track)           │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            Google Cloud Storage Public Bucket           │
│         (Serves 1080p video package worldwide)         │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Quickstart Guide

### 1. Installation
Clone the repository and install dependencies using `uv`:
```bash
git clone https://github.com/Prithvi-Naidu/buildwithgemini-tour-agent.git
cd buildwithgemini-tour-agent
uv sync
```

### 2. Environment Variables
Set your Google Cloud credentials:
```bash
export GOOGLE_CLOUD_PROJECT="qwiklabs-gcp-03-ae2ceb20cd60"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

### 3. Launch Local Agent Web UI
Run the local ADK server:
```bash
uv run adk web --port 8080
```
Open **`http://127.0.0.1:8080`** in your browser to interact with the tour agent!

---

## 📄 License
Licensed under the **Apache License, Version 2.0**.
