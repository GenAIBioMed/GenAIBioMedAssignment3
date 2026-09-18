# Scientific Analysis with AI Agent Workspaces

!!! abstract "Assignment Overview"

```
In this assignment, you will use a **science agent workspace** to complete three small but realistic computational biology tasks:

1. **Protein mutation analysis**
2. **Single-cell RNA-seq analysis and robustness testing**
3. **Spatial transcriptomics and spatial organization**

These tasks are designed to run on a **normal laptop**. You do not need a GPU, and you will not train any machine-learning models.

The goal is not simply to obtain an answer from an AI model. You will use an agent to **plan an analysis, execute code, inspect results, use scientific databases, test assumptions, and evaluate whether its conclusions are supported by evidence**.
```

---

## 1. Science Agent Workspaces

Large language models are increasingly being used as interactive scientific assistants. A science agent workspace extends a language model with tools that allow it to do more than answer questions in natural language.

A typical workspace may allow an agent to:

* read local files and datasets,
* search scientific literature and databases,
* write and execute Python or R,
* inspect intermediate results,
* generate figures and tables,
* revise an analysis when something goes wrong,
* maintain a record of how a result was produced.

The workflow therefore looks less like a normal chatbot conversation and more like a small interactive research environment:

```text
Research question
       ↓
Agent proposes a plan
       ↓
Search databases / literature
       ↓
Write and execute analysis code
       ↓
Inspect intermediate results
       ↓
Run additional checks or controls
       ↓
Generate figures and conclusions
       ↓
Human reviews the evidence
```

### Claude Science and GPT-Rosalind Workbench

**Claude Science** is Anthropic's scientific research workspace. It combines Claude with scientific tools, computational environments, files, databases, and external computing resources. A researcher can describe a scientific objective and interact with the agent while it performs a multi-step analysis.

**GPT-Rosalind / Rosalind Workbench** follows a similar idea with a stronger focus on life-science workflows. It is designed to help researchers work with biological data, scientific evidence, sequencing workflows, computational tools, and reusable analysis procedures.

Although their implementations differ, both systems illustrate the same important idea:

> ==A scientific agent should not only generate an answer. It should be able to perform and document the analysis that supports that answer.==

![Example of a science agent workspace](assets/images/science-agent-workspace.png)

*Example concept of a science agent workspace. Replace this image with a screenshot from Claude Science, Rosalind, or another system if desired.*

---

## 2. Open-Source Workspace: Synthetic Sciences OpenScience

For this assignment, the recommended open-source implementation is **Synthetic Sciences OpenScience**.

OpenScience provides a workspace in which an AI agent can interact with local files, computational environments, scientific resources, and external tools. Instead of manually switching between a chatbot, terminal, notebook, browser, and scientific databases, these capabilities can be coordinated through a single agent.

A simplified architecture is:

```text
                         ┌─────────────────┐
                         │ Research prompt │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ OpenScience     │
                         │ Agent           │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
       Literature / Web       Python / R        Scientific tools
          databases           execution          and databases
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                        Figures, tables, code,
                        evidence, and conclusions
```

This makes OpenScience particularly useful for this assignment because each of the three tasks requires the agent to combine **computation with scientific reasoning**.

!!! important "You are still responsible for the analysis"

```
OpenScience can generate code, select tools, interpret results, and search for evidence. None of these actions are guaranteed to be correct.

You should treat the agent as a **research assistant**, not as an authority.
```

---

## 3. Choosing a Model

OpenScience is the workspace, but it still requires an underlying language model.

=== "If you already have Claude or GPT access"

```
If you already have access to a strong Claude or GPT model that can be used for scientific or agentic workflows, we recommend using your existing subscription.

Stronger models generally perform better at:

- multi-step planning,
- choosing appropriate tools,
- debugging code,
- interpreting scientific results,
- recognizing when an analysis has failed.

You may still use OpenScience if you prefer the open-source workspace.
```

=== "If you want a free option"

````
You can use:

**OpenScience + OpenRouter + a free model**

**OpenRouter** provides a common API interface for many language models from different providers. Some models are available through free inference tiers.

The basic setup is:

```text
OpenScience
     ↓
OpenRouter API
     ↓
Free language model
```

Free models can be sufficient for this assignment, but their performance may vary considerably.

In particular, weaker models may have more difficulty with:

- long analysis plans,
- tool selection,
- debugging,
- interpreting biological results,
- keeping track of previous analysis steps.

!!! warning

    A model being free does **not** mean that it is appropriate for agent workflows.

    When selecting a model, prefer one that supports **tool use / function calling** and has a reasonably large context window.

    Free models available through OpenRouter can change over time, so you do not need to use the same model as other students.
````

---

## 4. Installing and Configuring OpenScience

You only need to complete this setup once.

### Install OpenScience

Choose one installation method.

=== "npm"

````
```bash
npm install -g @synsci/openscience
```

Start it with:

```bash
openscience
```
````

=== "Run without installing"

````
```bash
npx synsci
```
````

=== "macOS / Linux installer"

````
```bash
curl -fsSL https://openscience.sh/install | bash
```
````

Once OpenScience starts correctly, create a workspace for this assignment.

A simple directory structure is:

```text
science-agent-assignment/
├── protein/
├── single_cell/
└── spatial/
```

For example:

```bash
openscience ./protein
```

### Configure your model

OpenScience allows you to configure model providers from the interface or command line.

From the interface, open:

```text
Customize → Models
```

or use:

```bash
openscience keys add
```

If you are using OpenRouter, add your OpenRouter API key and select an appropriate model.

!!! danger "Never expose API keys"

```
Do **not** include API keys in:

- your report,
- screenshots,
- notebooks,
- GitHub repositories,
- submitted code,
- shared configuration files.
```

---

## 5. How to Work with the Agent

For all three tasks, we recommend the same general workflow.

Do **not** begin by asking the agent to produce a complete final report.

Instead, treat the analysis as an interactive process:

```text
1. Explain the scientific question
              ↓
2. Ask the agent to propose a plan
              ↓
3. Review the plan
              ↓
4. Let it perform the first analysis
              ↓
5. Inspect code, figures, and intermediate results
              ↓
6. Question weak or surprising results
              ↓
7. Ask for controls or additional analysis
              ↓
8. Decide which conclusions are actually supported
```

A useful first request is:

```text
Before running the analysis, propose a clear analysis plan.
Explain what data, software, databases, and statistical methods
you intend to use and why.
```

!!! tip "Interact with the agent"

```
Good use of a science agent should involve follow-up questions.

For example:

> Why did you choose this clustering parameter?

> What evidence supports this cell-type annotation?

> Can you test whether this result remains stable with another parameter?

> Is this conclusion computed from the data, or retrieved from a database?

> What would be an appropriate negative control?
```

The three tasks below are designed so that the **first result should not be the end of the analysis**.

---

# Task 1 — Predicting the Effects of Protein Mutations

## Scientific Question

You will be given a protein and several candidate missense mutations.

Your goal is to determine:

> **Which mutations are most likely to affect protein function, and what molecular mechanism could explain their effects?**

You should integrate multiple types of evidence rather than relying on a single prediction.

The overall reasoning should look like:

```text
Protein sequence
      +
Protein structure
      +
Functional annotations
      +
Scientific literature
      ↓
Evidence for each mutation
      ↓
Mechanistic hypothesis
```

---

## Suggested Analysis

Start by asking the agent to retrieve basic information about the protein. Relevant information may include its biological function, domains, catalytic residues, binding sites, ligands, and known structures.

Useful resources may include:

* UniProt,
* RCSB Protein Data Bank,
* AlphaFold Database,
* scientific literature.

Next, map the candidate mutations onto an appropriate structure.

For each mutation, investigate questions such as:

* Is the residue located inside an important domain?
* Is it close to a catalytic or functional residue?
* Is it close to a ligand or binding interface?
* Is the residue buried inside the protein or exposed to solvent?
* Does the mutation cause a major change in charge, polarity, or residue size?
* Is the structural region itself reliable?

Whenever possible, support these observations with **quantitative measurements**.

For example:

```text
Mutation → active-site distance
Mutation → ligand distance
Nearby residues within 5 Å
```

A statement such as:

> "This mutation is close to the active site."

is much weaker than:

> "The mutated residue is 4.1 Å from a catalytic residue and lies within the same conserved domain."

---

### Distinguish Observation from Interpretation

A major goal of this task is to separate what the data show from what you infer.

| Type                  | Example                                                                     |
| --------------------- | --------------------------------------------------------------------------- |
| **Observation**       | The residue is 4.1 Å from the bound ligand.                                 |
| **Prediction**        | The mutation may interfere with ligand binding.                             |
| **External evidence** | Previous studies report that this region contributes to ligand recognition. |

==Do not present a prediction as if it were directly observed.==

---

### Example Starting Prompt

```text
I want to evaluate how several missense mutations may affect this protein.

First create an analysis plan. Use protein sequence, structural information,
functional annotations, and scientific literature.

Whenever possible, perform quantitative structural analysis rather than
relying only on visual inspection.

For each mutation, clearly separate:
1. observations from the data,
2. mechanistic predictions,
3. external evidence.
```

You should modify your prompts as the analysis progresses.

---

### Expected Results

Your final protein analysis should include:

* a short description of the protein,
* a table comparing all candidate mutations,
* at least one structural visualization showing mutation locations,
* quantitative structural evidence where appropriate,
* a mechanistic interpretation of each mutation,
* supporting database or literature evidence.

A useful summary table might look like:

| Mutation   | Structural context | Quantitative evidence         | Interpretation       | Confidence |
| ---------- | ------------------ | ----------------------------- | -------------------- | ---------- |
| Mutation A | Near active site   | 4.1 Å from ligand             | May disrupt binding  | High       |
| Mutation B | Surface loop       | No nearby functional residues | Effect uncertain     | Low        |
| Mutation C | Protein core       | Multiple hydrophobic contacts | May destabilize fold | Moderate   |

![Example protein mutation visualization](assets/images/example-protein.png)

*Example of mutations mapped onto a protein structure.*

---

# Task 2 — Single-Cell Cell Types and Robustness

## Scientific Question

For this task, you will analyze the small **PBMC3k single-cell RNA-seq dataset**.

Your goal is not only to identify major immune-cell populations, but also to ask:

> **Which biological conclusions remain stable when reasonable analysis choices are changed?**

This makes the task different from simply reproducing a standard Scanpy tutorial.

---

## Build a Baseline Analysis

Ask the agent to develop a reasonable single-cell analysis workflow.

A typical workflow may contain:

```text
Expression matrix
      ↓
Quality control
      ↓
Normalization
      ↓
Highly variable genes
      ↓
PCA
      ↓
Cell-cell neighbor graph
      ↓
Clustering
      ↓
Marker genes
      ↓
Cell-type annotation
```

You do not need to tell the agent every Scanpy command.

Part of the assignment is evaluating whether the agent chooses and correctly implements a reasonable workflow.

Once clusters have been identified, use **marker genes derived from the data** to annotate major cell populations.

The reasoning should follow:

```text
Observed cluster
      ↓
Marker genes from the dataset
      ↓
Possible biological identity
      ↓
Database / literature evidence
      ↓
Final annotation
```

!!! warning

```
Do not accept a cell-type label simply because the agent produced it.

The annotation should be supported by the expression pattern of biologically meaningful marker genes.
```

---

## Test Whether the Result Is Robust

After obtaining a reasonable baseline result, change the clustering conditions.

For example, compare several Leiden resolutions:

```text
resolution = 0.3
resolution = 0.6
resolution = 1.0
```

You are not trying to find one "correct" resolution.

Instead, ask:

* Which populations appear consistently?
* Which clusters split at higher resolution?
* Which populations merge at lower resolution?
* Do the biological annotations remain stable?

Next, perform a simple **downsampling experiment**.

For example, randomly retain approximately 70% of the cells and repeat the analysis.

Compare the downsampled result with the original analysis using appropriate evidence such as:

* cluster composition,
* marker genes,
* cell-type annotations,
* ARI,
* NMI.

You do not need to use every possible metric. Choose comparisons that help answer the biological question.

---

## Investigate an Ambiguous Population

Select at least one population that is difficult to annotate or unstable across your analyses.

Investigate why.

Possible explanations include:

* closely related cell types,
* shared marker genes,
* continuous biological states,
* small population size,
* technical noise,
* sensitivity to clustering parameters.

This part is important because real biological data rarely produce perfectly separated groups.

!!! question "Think biologically"

```
If two populations are difficult to separate, do not immediately conclude that the clustering algorithm failed.

Ask whether the biology itself may represent a continuum rather than two sharply separated cell types.
```

---

### Example Starting Prompt

```text
Analyze the PBMC3k dataset and identify its major cell populations.

Do not use predefined cell labels.

First propose a reasonable single-cell analysis plan. Use marker genes
derived from the data to support each annotation.

After obtaining a baseline result, test whether the main biological
conclusions remain stable when clustering parameters are changed and
when the dataset is downsampled.

Finally, identify at least one ambiguous or unstable population and
investigate why it is difficult to separate.
```

---

### Expected Results

Your final single-cell analysis should include:

* an annotated UMAP,
* marker-gene evidence for the major populations,
* a comparison across several clustering parameters,
* a downsampling robustness analysis,
* a discussion of at least one ambiguous population.

A useful summary table might be:

| Cell population | Main marker genes | Stable across resolutions? | Stable after downsampling? | Notes                     |
| --------------- | ----------------- | -------------------------- | -------------------------- | ------------------------- |
| Population A    | ...               | Yes                        | Yes                        | Clearly separated         |
| Population B    | ...               | Mostly                     | Yes                        | Splits at high resolution |
| Population C    | ...               | No                         | No                         | Ambiguous population      |

![Example single-cell analysis](assets/images/example-single-cell-umap.png)

*Example visualization of cell populations in a UMAP embedding.*

The final discussion should answer:

> **Which biological conclusions are robust, and which depend strongly on analytical choices?**

---

# Task 3 — Spatial Transcriptomics and Non-Random Tissue Organization

## Scientific Question

For the final task, you will work with a small spatial transcriptomics dataset, such as a Visium example dataset available through Squidpy.

The central question is:

> **Do transcriptionally defined tissue domains correspond to genuine non-random spatial organization?**

This task combines expression analysis, spatial statistics, visualization, and a simple null experiment.

---

## First Identify Domains Without Using Spatial Coordinates

Begin by clustering spots using only gene-expression information.

Do **not** use spatial coordinates during this step.

A reasonable workflow may look like:

```text
Gene expression
      ↓
Feature selection
      ↓
PCA
      ↓
Expression-based neighbor graph
      ↓
Clustering
```

These groups are therefore defined by their transcriptional profiles rather than their physical locations.

Once the clusters have been identified, plot the same cluster labels using the true spatial coordinates.

You can now compare:

```text
Expression space                Physical tissue space
      ↓                                  ↓
Which spots have                Where are those spots
similar expression?             located in the tissue?
```

Ask whether the expression-defined domains:

* form clear spatial regions,
* appear spatially mixed,
* have recognizable boundaries,
* tend to occur next to specific other domains.

![Example spatial transcriptomics domains](assets/images/example-spatial-clusters.png)

*Example of transcriptionally defined clusters projected back onto tissue coordinates.*

---

## Quantify Spatial Organization

Visual inspection is useful, but it is not sufficient.

Use an appropriate quantitative spatial method such as:

* neighborhood enrichment,
* Moran's I,
* spatial autocorrelation,
* another justified spatial statistic.

The agent should explain what the statistic measures and why it is relevant to the question.

For example, if a cluster strongly neighbors itself in physical space, this provides quantitative evidence that the transcriptional domain is spatially coherent.

---

## Identify Spatially Variable Genes

Next, identify genes whose expression has strong spatial organization.

For example:

```text
Strong spatial pattern           Weak spatial pattern

████████                          █░██░█░█
████████                          ░█░░██░█
░░░░░░░░                          ██░█░░██
░░░░░░░░                          ░██░█░░█
```

To keep the analysis lightweight, it is reasonable to restrict this analysis to approximately **100–300 highly variable genes**.

---

## Compare Differential Expression with Spatial Variation

A gene can be a strong cluster marker without having the strongest spatial pattern.

Likewise, a spatially organized gene may not be one of the top differential-expression markers.

Compare:

```text
Differential-expression ranking
                vs.
Spatial-autocorrelation ranking
```

Identify examples of genes that are:

1. strong in both rankings,
2. strong differential-expression markers but weak spatial genes,
3. strong spatial genes but weaker differential-expression markers.

Explain why these two analyses measure different properties.

---

## Build a Negative Control

Finally, test whether the observed spatial organization is stronger than expected by chance.

Design a simple randomization experiment.

For example:

```text
Original coordinates
       ↓
Spatial statistic
```

compared with:

```text
Randomly permuted coordinates
       ↓
Same spatial statistic
```

Another reasonable control is to shuffle cluster labels while keeping the spatial graph fixed.

The important point is that the **same statistic** should be evaluated on the original and randomized data.

!!! success "What the control should tell you"

```
If the original dataset contains genuine spatial organization, the spatial signal should generally be stronger than the signal obtained after randomization.

This does not prove a biological mechanism, but it provides evidence that the observed pattern is not simply produced by the analysis pipeline.
```

---

### Example Starting Prompt

```text
I want to determine whether transcriptionally defined tissue domains
show genuine spatial organization.

First cluster the spots using gene expression without using spatial
coordinates.

Then project those clusters back into physical tissue space and quantify
their spatial organization using an appropriate spatial statistic.

Identify spatially variable genes and compare them with genes identified
through differential expression.

Finally, design a randomized negative control and compare the spatial
signal before and after randomization.

Clearly distinguish results directly supported by the data from
biological interpretations.
```

---

### Expected Results

Your final spatial transcriptomics analysis should include:

* expression-based clustering,
* visualization of those clusters in tissue coordinates,
* quantitative analysis of spatial organization,
* several spatially variable genes,
* comparison between differential-expression and spatial rankings,
* a randomized negative control.

A useful final comparison might look like:

| Analysis            | Original data | Randomized control |
| ------------------- | ------------: | -----------------: |
| Spatial statistic A |           ... |                ... |
| Spatial statistic B |           ... |                ... |

The final discussion should answer:

> **Does transcriptional identity correspond to non-random spatial tissue organization?**

Your conclusion should be supported by both **visual evidence and quantitative evidence**.

---

# 6. What You Need to Submit

Submit **one short report** containing all three analyses, together with the important analysis files used to generate your results.

A suggested directory structure is:

```text
submission/
├── report.pdf
│
├── protein/
│   ├── analysis code
│   └── important outputs
│
├── single_cell/
│   ├── analysis code
│   └── important outputs
│
└── spatial/
    ├── analysis code
    └── important outputs
```

You do not need to include package caches, temporary downloads, or other unnecessary files.

---

## Required Report Content

=== "Protein"

```
Include:

- protein and mutation information,
- mutation comparison table,
- structural visualization,
- quantitative structural evidence,
- mechanistic interpretation,
- external database or literature evidence.
```

=== "Single-cell"

```
Include:

- annotated UMAP,
- marker-gene evidence,
- clustering robustness comparison,
- downsampling analysis,
- discussion of one ambiguous population.
```

=== "Spatial transcriptomics"

```
Include:

- expression-based clustering,
- spatial visualization,
- quantitative spatial statistics,
- spatially variable genes,
- comparison with differential-expression genes,
- randomized negative control.
```

---

# 7. Agent Audit

For each of the three tasks, include a short **Agent Audit** section.

The goal is to show that you understand what the agent actually did rather than simply accepting its final answer.

Address the following four questions.

### 1. What resources did the agent use?

List the important:

* datasets,
* databases,
* software packages,
* websites,
* scientific papers.

### 2. What did the agent actually compute?

Separate calculations from retrieved information.

For example:

| Computed by the agent      | Retrieved from external sources |
| -------------------------- | ------------------------------- |
| PCA                        | UniProt annotations             |
| Leiden clustering          | PDB structure                   |
| Moran's I                  | Literature evidence             |
| Residue-to-ligand distance | Known functional residues       |

### 3. What did you independently verify?

Provide at least one example for each task.

### 4. What did the agent do poorly?

Identify at least one:

* incorrect result,
* questionable methodological choice,
* unsupported statement,
* misleading visualization,
* unnecessary analysis,
* weak assumption.

Explain what you noticed and how you evaluated or corrected it.

!!! important

```
You are **expected** to identify at least one weakness in the agent's analysis.

Finding and correcting a problem is evidence that you used the system critically.
```

---

# 8. What We Are Looking For

This assignment is not primarily about producing the most polished AI-generated report.

We are interested in whether you can use an AI agent to carry out a scientifically reasonable and reproducible analysis.

| Component               | What matters                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| **Scientific workflow** | Were reasonable analysis steps chosen and correctly executed?            |
| **Evidence**            | Are the conclusions supported by data and appropriate external evidence? |
| **Robustness**          | Did you test whether important results depend on arbitrary choices?      |
| **Reproducibility**     | Is it clear how figures and conclusions were produced?                   |
| **Agent audit**         | Did you critically inspect and evaluate the agent's work?                |

The most important distinction throughout the assignment is:

> ==What did the data show, what did the agent infer, and what was supported by external scientific evidence?==

A good submission should make these three levels clear.
