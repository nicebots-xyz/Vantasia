<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">VANTASIA</h1>
</p>
<p align="center">
    <em>Vantasia: Docking Your Code into Seamless Deployments</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/nicebots-xyz/Vantasia?style=flat-square&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/nicebots-xyz/Vantasia?style=flat-square&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/nicebots-xyz/Vantasia?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/nicebots-xyz/Vantasia?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>     - [⚙️ Installation](#-installation)
>     - [🤖 Running Vantasia](#-running-Vantasia)
>     - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Vantasia is a Python-based application streamlined to operate within Docker containers, ensuring environmental consistency and ease of deployment. It focuses on robustness by installing necessary system dependencies and build tools, while also addressing security by running as a non-root user. The project leverages Docker's caching mechanism for efficient builds and integrates CockroachDB for data management, highlighted by the inclusion of database certificate handling. Vantasia appears to target users seeking a scalable, secure, and containerized Python service that can interact seamlessly with a modern, distributed SQL database system.

---

## 📦 Features

|    | Feature            | Description                                                           |
|----|--------------------|-----------------------------------------------------------------------|
| ⚙️ | **Architecture**   | *Unclear based on given data. A typical Python project structure.*    |
| 🔩 | **Code Quality**   | *Cannot be assessed without seeing the code. Expect PEP 8 adherence.* |
| 📄 | **Documentation**  | *Minimal documentation inferred from Dockerfile comments.*            |
| 🔌 | **Integrations**   | *Integrations with various APIs like OpenAI, Twitch, and YouTube.*    |
| 🧩 | **Modularity**     | *Modular Python files suggest organized code, but further analysis is required.* |
| 🧪 | **Testing**        | *No explicit mention of testing frameworks or tools.*                 |
| ⚡️ | **Performance**    | *Cannot be assessed without performance metrics. Python's efficiency varies.* |
| 🛡️ | **Security**       | *No explicit security measures detailed. Python's environment isolation in Docker is one layer.* |
| 📦 | **Dependencies**   | *Relies on popular libraries such as requests, SQLAlchemy, pydantic.* |
| 🚀 | **Scalability**    | *Scalability potential hinges on the underlying architecture and database design.* |


---

## 📂 Repository Structure

```sh
└── Vantasia/
    ├── Dockerfile
    ├── docker-compose.yaml
    ├── main.py
    ├── requirements.txt
    └── src
        ├── chore
        │   └── BestOfProcessor.py
        ├── config
        │   ├── anthropic_prompt.txt
        │   ├── dbinit.sql
        │   ├── openai_prompt.txt
        │   └── settings.py
        ├── downloaders
        │   ├── twitch_downloader.py
        │   └── youtube_downloader.py
        ├── extensions
        │   └── bestof.py
        ├── models
        │   ├── base.py
        │   ├── bestof.py
        │   ├── channel.py
        │   ├── user.py
        │   └── video.py
        ├── processors
        │   ├── anthropic_processor.py
        │   ├── timeline_maker.py
        │   └── whisper_processor.py
        └── utils
            ├── db_utils.py
            └── formatTranscript.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                            | Summary                                                                                                                                                                                                           |
| ---                                                                                             | ---                                                                                                                                                                                                               |
| [Dockerfile](https://github.com/nicebots-xyz/Vantasia/blob/master/Dockerfile)                   | This Dockerfile sets up a Python environment for the Vantasia app, focusing on dependency management and secure, non-root execution within a containerized setup.                                                 |
| [docker-compose.yaml](https://github.com/nicebots-xyz/Vantasia/blob/master/docker-compose.yaml) | This `docker-compose.yaml` defines a Docker service for a Discord bot, with volume configuration for persistent data and environment variable management, within the Vantasia multimedia processing architecture. |
| [requirements.txt](https://github.com/nicebots-xyz/Vantasia/blob/master/requirements.txt)       | The `requirements.txt` file lists dependencies necessary for the functioning of the Vantasia content processing and management application, impacting the project's setup and environment.                        |
| [main.py](https://github.com/nicebots-xyz/Vantasia/blob/master/main.py)                         | This `main.py` initializes a Discord bot for Vantasia, handling events, logging in, setting its presence, and loading the BestOf extension module.                                                                |

</details>

<details closed><summary>src.extensions</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                    |
| ---                                                                                        | ---                                                                                                                                                                                                                                                        |
| [bestof.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/extensions/bestof.py) | The `bestof.py` extension integrates a Discord bot with commands for user interaction, database session handling, terms of service acceptance, and bestof content creation facilitated by the BestOfProcessor, conforming to the Discord.py cog structure. |

</details>

<details closed><summary>src.config</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                       |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                           |
| [settings.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/config/settings.py)                   | This module configures global settings for database, Discord, file paths, and AI services, impacting overall application functionality.                                                                                                                                                       |
| [openai_prompt.txt](https://github.com/nicebots-xyz/Vantasia/blob/master/src/config/openai_prompt.txt)       | The openai_prompt.txt serves as instructions for an AI to process and condense transcripts from YouTube/Twitch streams into engaging, informative summaries suitable for standalone videos, while addressing speech-to-text inaccuracies. It integrates within a content processing workflow. |
| [dbinit.sql](https://github.com/nicebots-xyz/Vantasia/blob/master/src/config/dbinit.sql)                     | This SQL script initializes the database schema for the Vantasia application, outlining essential tables and relationships for storing users, videos, and curated highlights.                                                                                                                 |
| [anthropic_prompt.txt](https://github.com/nicebots-xyz/Vantasia/blob/master/src/config/anthropic_prompt.txt) | The `anthropic_prompt.txt` file specifies instructions for transforming stream transcripts into concise, informative XML segments, aiding in content distillation for the Vantasia repository's processing tasks.                                                                             |

</details>

<details closed><summary>src.chore</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [BestOfProcessor.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/chore/BestOfProcessor.py) | This `BestOfProcessor.py` integrates Discord UI components for video processing workflows, including user interaction for frame rate selection and TOS acceptance, within a comprehensive media processing platform built around a Discord bot. It leverages async database operations, video downloading, transcript generation, and best-of clip compilation, conditioned on user permissions and content ownership verification. |

</details>

<details closed><summary>src.processors</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                       |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                           |
| [timeline_maker.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/processors/timeline_maker.py)           | The `timeline_maker.py` generates video/audio timelines from transcripts, integrating selected parts into an editable OTIO JSON format.                                                                                                       |
| [anthropic_processor.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/processors/anthropic_processor.py) | The `anthropic_processor.py` integrates AI language models (Anthropic and OpenAI) for processing transcripts in the Vantasia repository, transforming input data between JSON and XML formats. It aims to generate best of content summaries. |
| [whisper_processor.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/processors/whisper_processor.py)     | Transcribes audio files using OpenAI Whisper, returning verbose JSON metadata. Integral to content processing within Vantasia's architecture.                                                                                                 |

</details>

<details closed><summary>src.utils</summary>

| File                                                                                                      | Summary                                                                                                                                                                                              |
| ---                                                                                                       | ---                                                                                                                                                                                                  |
| [formatTranscript.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/utils/formatTranscript.py) | The `formatTranscript` function in `src/utils/formatTranscript.py` within the Vantasia repository enhances transcript readability, rearranging raw segment data into a simplified dictionary format. |
| [db_utils.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/utils/db_utils.py)                 | This code snippet establishes a utility for asynchronous database interaction, integrating with models to initialize and manage the data layer within the Vantasia service-oriented architecture.    |

</details>

<details closed><summary>src.models</summary>

| File                                                                                     | Summary                                                                                                                                                          |
| ---                                                                                      | ---                                                                                                                                                              |
| [base.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/models/base.py)       | This script establishes the asynchronous database connection backbone for the Vantasia repository, enabling ORM-based interactions with the database.            |
| [channel.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/models/channel.py) | The `channel.py` defines the ORM mapping for a Channels table, linking channels to users within the Vantasia service's data layer.                               |
| [bestof.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/models/bestof.py)   | The BestOf class in src/models/bestof.py defines a database model for curated video highlights within the Vantasia system, relating to users and videos.         |
| [video.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/models/video.py)     | The `Video` class in `video.py` defines the data model for video entities, including storage and BestOfs relation within the Vantasia service's database schema. |
| [user.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/models/user.py)       | The `user.py` script defines a User model, linking to Users table with relationships to BestOf and Channel in the Vantasia app's database schema.                |

</details>

<details closed><summary>src.downloaders</summary>

| File                                                                                                                | Summary                                                                                                                                                                              |
| ---                                                                                                                 | ---                                                                                                                                                                                  |
| [twitch_downloader.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/downloaders/twitch_downloader.py)   | This twitch_downloader.py script is planned for asynchronous video downloads from Twitch, contributing to the media processing functionality of the Vantasia repository.             |
| [youtube_downloader.py](https://github.com/nicebots-xyz/Vantasia/blob/master/src/downloaders/youtube_downloader.py) | The `youtube_downloader.py` component in Vantasia handles asynchronous YouTube video downloading, specifically extracting audio, and saving it within a defined directory structure. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### ⚙️ Installation

1. Clone the Vantasia repository:

```sh
git clone https://github.com/nicebots-xyz/Vantasia
```

2. Change to the project directory:

```sh
cd Vantasia
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running Vantasia

Use the following command to run Vantasia:

```sh
python main.py
```

### 🧪 Tests

To execute tests, run:

```sh
pytest
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/nicebots-xyz/Vantasia/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/nicebots-xyz/Vantasia/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/nicebots-xyz/Vantasia/issues)**: Submit bugs found or log feature requests for Vantasia.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/nicebots-xyz/Vantasia
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
