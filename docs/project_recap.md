AI Personal Knowledge Engine — Project Recap
Obiettivo del progetto

Realizzare un Second Brain personale basato su AI, con l'obiettivo di imparare in modo pratico le tecnologie più richieste per il ruolo di AI Engineer.

Il progetto sarà sviluppato in maniera incrementale, comprendendo i concetti fondamentali invece di utilizzare framework che nascondono la complessità.

Obiettivi finali:

organizzare documenti e conoscenza personale;
ricerca semantica;
gestione degli embeddings;
Vector Database;
Retrieval Augmented Generation (RAG);
API REST con FastAPI;
interfaccia utente.
Setup completato
Repository GitHub

Repository creata:

ai-personal-knowledge-engine

Repository inizializzata con:

README
LICENSE
.gitignore
Struttura del progetto
ai-personal-knowledge-engine/

├── docs/
├── notebooks/
├── src/
│   └── ai_brain/
│       ├── __init__.py
│       ├── main.py
│       └── embeddings/
│           ├── __init__.py
│           └── service.py
│
├── tests/
│
├── requirements.txt
├── pyproject.toml
└── README.md
Ambiente Python

Creazione virtual environment

python -m venv .venv

Attivazione

Windows

.venv\Scripts\activate

Verifica

python --version

Verifica ambiente

where python

Il percorso deve puntare a:

.venv\Scripts\python.exe
Gestione dipendenze

Installazione librerie

pip install fastapi uvicorn
pip install pytest
pip install python-dotenv
pip install jupyter notebook
pip install numpy pandas scikit-learn sentence-transformers

Aggiornamento requirements

pip freeze > requirements.txt

Visualizzare librerie installate

pip list
Configurazione progetto Python

Creato

pyproject.toml

Installazione package locale

pip install -e .

Questo permette import del tipo

from ai_brain.main import app

senza modificare il PYTHONPATH.

Backend

Creato backend FastAPI.

Avvio

uvicorn ai_brain.main:app --reload

Indirizzi

http://127.0.0.1:8000

Swagger

http://127.0.0.1:8000/docs
Testing

Creati test automatici.

Esecuzione

pytest

Risultato

2 passed
Git

Controllo modifiche

git status

Aggiunta file

git add .

Commit

git commit -m "messaggio"

Invio su GitHub

git push

Storico

git log --oneline

Differenze

git diff
Primo notebook AI

Creato

notebooks/01_embeddings.ipynb

Obiettivo

Comprendere il funzionamento degli embeddings.

Librerie utilizzate

NumPy
Pandas
Sentence Transformers
Scikit-learn

Modello utilizzato

all-MiniLM-L6-v2
Primo esperimento

Trasformazione di tre frasi in embeddings.

Output ottenuto

(3, 384)

Interpretazione

3 frasi
ogni frase è rappresentata da un vettore di 384 dimensioni
Similarità semantica

Utilizzo di

cosine_similarity()

per confrontare il significato delle frasi.

Concetto fondamentale imparato

Testo

↓

Embedding

↓

Vettore numerico

↓

Confronto matematico

Questa è la base di:

Semantic Search
Vector Database
RAG
Primo componente del progetto

Creato

EmbeddingService

File

src/ai_brain/embeddings/service.py

Responsabilità

caricare il modello;
generare embeddings;
calcolare la similarità.

In questo modo il notebook rimane un ambiente di sperimentazione, mentre il codice riutilizzabile vive in src/.

Cosa ho imparato
Python
Virtual Environment
struttura professionale con src
package Python
testing con pytest
Backend
FastAPI
organizzazione del progetto
API REST
AI
Sentence Transformers
Embeddings
Cosine Similarity
rappresentazione vettoriale del testo
Software Engineering
separazione tra prototipo e codice di produzione;
test automatici;
Git workflow.
Roadmap del progetto
Sprint 1 (in corso)
✅ setup del progetto
✅ notebook embeddings
✅ EmbeddingService
⏳ rifinitura del servizio
Sprint 2

Document Loader

Obiettivo

Leggere documenti reali.

Supporto a:

TXT
Markdown
PDF

Creare il componente

DocumentLoader
Sprint 3

Vector Database

Introduzione di:

ChromaDB oppure FAISS

Obiettivo

Memorizzare e recuperare embeddings.

Sprint 4

Semantic Search

Creare un motore di ricerca sui documenti.

Workflow

Domanda

↓

Embedding

↓

Vector Search

↓

Documenti più rilevanti
Sprint 5

RAG

Integrare un LLM.

Workflow

Domanda

↓

Retrieval

↓

LLM

↓

Risposta
Sprint 6

Backend completo

API come:

POST /documents

POST /search

POST /ask
Sprint 7

Interfaccia utente

Probabilmente Streamlit.

Filosofia del progetto

L'obiettivo non è costruire un chatbot.

L'obiettivo è comprendere e implementare uno per uno tutti i componenti di un moderno sistema AI:

Documenti

↓

Embeddings

↓

Vector Database

↓

Semantic Search

↓

Retrieval

↓

LLM

↓

Applicazione
La mia valutazione

Ti faccio anche un feedback sul percorso fin qui.

Secondo me hai affrontato la parte più difficile del progetto: impostare basi solide. Molti iniziano direttamente con LangChain o con un tutorial, ottenendo qualcosa che funziona ma senza capire davvero come è costruito.

Noi abbiamo fatto il contrario: abbiamo costruito un progetto che cresce in modo professionale, con Git, test, struttura src, notebook per la sperimentazione e componenti riutilizzabili. È un approccio più lento all'inizio, ma tra qualche mese farà una differenza enorme nel tuo portfolio e nella tua preparazione per un ruolo da AI Engineer.

La prossima volta inizieremo a lavorare con documenti reali. Da lì il progetto smetterà di essere un esercizio sugli embeddings e inizierà a diventare il tuo vero AI Personal Knowledge Engine.




# Sessione - Sprint 2 / Introduzione Semantic Search

## Data
18/07/2026

---

# Obiettivo della sessione

Continuare la costruzione della pipeline AI del progetto.

Obiettivo principale:

- completare la fase di indicizzazione della knowledge base;
- progettare il futuro sistema di ricerca semantica;
- introdurre il concetto di query embedding;
- preparare la struttura per implementare la semantic search.

---

# Stato iniziale

Prima della sessione il progetto era in grado di:

- caricare documenti Markdown;
- trasformarli in oggetti Document;
- generare embeddings tramite EmbeddingService;
- salvare documenti ed embeddings in `data/knowledge_base.json`.

Pipeline precedente:


Documenti Markdown

    |
    v

DocumentLoader

    |
    v

Document

    |
    v

EmbeddingService

    |
    v

DocumentEmbedding

    |
    v

knowledge_base.json


---

# Decisioni architetturali prese

## 1. Separazione delle responsabilità

Abbiamo deciso di mantenere separati:

- creazione embeddings;
- gestione documenti;
- persistenza;
- ricerca.

Motivazione:

Evitare servizi troppo complessi con troppe responsabilità.

Principio applicato:

> Ogni componente deve avere una responsabilità chiara.

---

# Creazione modulo Knowledge

È stato creato:


src/ai_brain/knowledge/

├── init.py
├── models.py
└── repository.py


---

# Nuovo modello: DocumentEmbedding

File:


knowledge/models.py


Creato il modello:

```python
@dataclass
class DocumentEmbedding:
    document: Document
    embedding: list[float]
Motivazione

Separare:

il documento originale;
la sua rappresentazione matematica.

Un documento contiene informazioni leggibili dall'uomo.

Un embedding contiene una rappresentazione numerica utilizzabile dagli algoritmi AI.

Esempio:

Document

{
 title:
 content:
}


+

Embedding

[
0.123,
0.456,
...
]

=

DocumentEmbedding
Creazione KnowledgeRepository

File:

knowledge/repository.py

Responsabilità:

Gestire la persistenza della knowledge base.

Attualmente utilizza:

JSON

File generato:

data/knowledge_base.json
Perché JSON?

Non è la soluzione definitiva.

In futuro verrà probabilmente sostituito da:

ChromaDB;
FAISS;
Qdrant;
Pinecone.

È stato scelto perché:

semplice;
facilmente ispezionabile;
utile per capire il funzionamento interno della pipeline.
Creazione KnowledgeService

Creato il servizio che orchestra:

DocumentLoader

        |
        v

EmbeddingService

        |
        v

DocumentEmbedding

        |
        v

KnowledgeRepository

Responsabilità:

Coordinare il processo completo di creazione della knowledge base.

Non implementa direttamente:

caricamento file;
generazione embeddings;
salvataggio.

Utilizza i servizi dedicati.

Introduzione Semantic Search

Abbiamo iniziato la progettazione del modulo:

src/ai_brain/search/

├── __init__.py
└── service.py
Concetto introdotto: Query Embedding

Una ricerca semantica non confronta direttamente:

testo query

contro

testo documenti

ma trasforma entrambi in vettori.

Esempio:

Query:

"Come posso imparare Python?"

diventa:

[
0.123,
0.456,
...
]

Successivamente viene confrontata con gli embeddings già salvati.

Decisione sul risultato della ricerca

Per la prima versione il metodo:

search(query)

restituirà:

[
    ("python", 0.91),
    ("machine_learning", 0.72)
]

Motivazione:

semplice da analizzare;
permette di capire il comportamento del modello;
facilita debugging e test.

In futuro potrà evolvere in un oggetto:

SearchResult

contenente:

documento;
score;
metadata.
Libreria scelta per Similarity Search

Per il confronto tra embeddings verrà utilizzata:

scikit-learn

con:

sklearn.metrics.pairwise.cosine_similarity

Motivazione:

La cosine similarity è una metrica molto utilizzata per confrontare embeddings perché misura la vicinanza semantica tra vettori.

Struttura futura della Semantic Search
User Query

      |
      v

EmbeddingService

      |
      v

Query Embedding

      |
      v

Confronto con embeddings salvati

      |
      v

Cosine Similarity

      |
      v

Ranking risultati

      |
      v

Top-K documents
Concetti AI introdotti

Durante questa sessione sono stati introdotti:

embeddings;
query embeddings;
semantic search;
cosine similarity;
similarity ranking;
pipeline RAG (Retrieval Augmented Generation).
Prossimi step
Step 1

Implementare:

KnowledgeRepository.load()

per leggere:

data/knowledge_base.json

e ricostruire:

DocumentEmbedding[]
Step 2

Completare:

SearchService

Implementando:

caricamento knowledge base;
embedding della query;
cosine similarity;
ordinamento risultati.
Step 3

Creare test automatici:

Esempio:

Query:

"voglio programmare in Python"

Aspettarsi:

python.md

come primo risultato.

Stato progetto

Completato:

✅ Setup progetto
✅ FastAPI base
✅ EmbeddingService
✅ DocumentLoader
✅ Document model
✅ DocumentEmbedding model
✅ KnowledgeRepository save
✅ KnowledgeService pipeline iniziale

In sviluppo:

🚧 Semantic Search


---

# Recap — Sprint 3: Semantic Search

## Obiettivo dello Sprint

Implementare una prima versione di **Semantic Search**:

> data una query in linguaggio naturale, trovare i documenti semanticamente più simili utilizzando gli embedding.

La pipeline realizzata è:

```text
Query utente
    ↓
EmbeddingService
    ↓
Embedding della query
    ↓
KnowledgeRepository.load()
    ↓
Embedding dei documenti già salvati
    ↓
Cosine Similarity
    ↓
Ranking
    ↓
Top-K risultati
```

---

## 1. KnowledgeRepository.load()

Abbiamo completato il metodo `load()` in:

```text
src/ai_brain/knowledge/repository.py
```

Il metodo legge:

```text
data/knowledge_base.json
```

e ricostruisce gli oggetti `DocumentEmbedding`.

Il flusso inverso rispetto a `save()` è:

```text
JSON
 ↓
dict
 ↓
Document
 ↓
DocumentEmbedding
```

Importante: `load()` **non genera nuovamente gli embedding**.

Gli embedding sono già presenti nel JSON perché sono stati generati durante la costruzione della knowledge base.

### Verifica manuale

Abbiamo verificato che i documenti venissero caricati correttamente e che gli embedding mantenessero la dimensione di 384.

Esempio:

```text
Documenti caricati: 4
Python
Embedding dimension: 384
Java
Embedding dimension: 384
Machine Learning
Embedding dimension: 384
Pizza
Embedding dimension: 384
```

---

## 2. SearchService

Abbiamo completato:

```text
src/ai_brain/search/service.py
```

Il `SearchService` si occupa di:

1. caricare la knowledge base;
2. trasformare la query in embedding;
3. recuperare gli embedding dei documenti;
4. calcolare la cosine similarity;
5. associare ogni documento al proprio score;
6. ordinare i risultati dal più simile al meno simile;
7. restituire i primi `top_k`.

La ricerca restituisce attualmente risultati nella forma:

```python
[
    ("python", 0.58),
    ("pizza", 0.34),
    ("java", 0.27)
]
```

Abbiamo scelto volutamente una struttura semplice invece di introdurre subito una classe `SearchResult`.

---

## 3. Cosine Similarity

Per confrontare gli embedding abbiamo utilizzato Scikit-learn:

```python
from sklearn.metrics.pairwise import cosine_similarity
```

Non abbiamo implementato manualmente la formula perché Scikit-learn fornisce già una soluzione affidabile e standard.

La cosine similarity misura quanto due vettori sono orientati nella stessa direzione nello spazio degli embedding.

Importante:

```text
0.58
```

non significa "58% di certezza".

È un **punteggio di similarità**, utilizzato per confrontare e ordinare i documenti.

---

## 4. Test della Semantic Search

Abbiamo creato:

```text
tests/test_search_service.py
```

con un test che verifica che una query relativa a Python restituisca `python` come documento più rilevante.

Il test verifica il comportamento:

```python
assert len(results) > 0
assert results[0][0] == "python"
```

Non verifichiamo il valore esatto dello score perché il punteggio potrebbe variare leggermente in base alle versioni delle librerie o del modello.

### Risultato

Tutti i test passano:

```text
100% passed
```

---

## 5. Verifica manuale

Abbiamo testato:

```text
"Come funziona Python?"
```

ottenendo:

```text
python 0.5879818633057421
pizza 0.34440421553825895
java 0.272665288423344...
```

Il risultato conferma che la semantic search sta funzionando: il documento `python` viene classificato come il più rilevante.

---

## 6. Warning Hugging Face

Durante l'esecuzione è comparso:

```text
Warning: You are sending unauthenticated requests to the HF Hub.
Please set a HF_TOKEN...
```

Non è un errore.

Il modello è stato comunque scaricato e utilizzato correttamente.

Per il momento non è necessario configurare un token Hugging Face.

---

# Concetti acquisiti

Durante questo sprint abbiamo utilizzato concretamente:

* **Sentence Transformers** → generazione degli embedding;
* **NumPy** → gestione dei vettori;
* **Scikit-learn** → cosine similarity;
* **JSON** → persistenza della knowledge base;
* **Repository pattern** → separazione della persistenza;
* **Service** → orchestrazione della logica applicativa;
* **pytest** → test automatici;
* **Semantic Search** → ricerca basata sul significato anziché sulle sole keyword.

---

# Stato del progetto

A questo punto il progetto è in grado di:

```text
1. leggere documenti
2. generare embedding
3. salvare gli embedding
4. ricaricarli
5. ricevere una query
6. generare l'embedding della query
7. confrontarlo con gli embedding dei documenti
8. classificare i documenti per similarità
```

La parte di **Semantic Search fondamentale è completata**.

---

# Prossimo Sprint — RAG + LLM

Il prossimo obiettivo sarà trasformare la Semantic Search in un sistema **RAG (Retrieval-Augmented Generation)**.

La nuova pipeline sarà:

```text
Domanda utente
      ↓
Semantic Search
      ↓
Documenti rilevanti
      ↓
Context
      ↓
LLM
      ↓
Risposta
```

Per il momento abbiamo volutamente evitato LangChain.

Questo ci permette di capire prima cosa succede realmente sotto il cofano.

Nel prossimo sprint introdurremo il concetto di **RAG** e successivamente valuteremo dove LangChain può semplificare la pipeline senza nascondere i concetti fondamentali.



# AI Personal Knowledge Engine — Project Recap

## Sprint 4 — RAG + Local LLM

### Obiettivo

Collegare la semantic search al modello linguistico locale per ottenere una prima pipeline **RAG (Retrieval-Augmented Generation)** funzionante.

L'obiettivo era capire il funzionamento della RAG manualmente, senza introdurre ancora LangChain.

---

# 1. SearchResult

Abbiamo modificato il risultato della ricerca semantica.

Prima:

```python
("python", 0.58)
```

Ora:

```python
SearchResult(
    document=document,
    score=0.58
)
```

con:

```python
@dataclass
class SearchResult:
    document: Document
    score: float
```

### Perché?

Perché per una RAG non basta sapere quale documento è rilevante.

Dobbiamo anche avere accesso al suo contenuto:

```python
result.document.content
```

Questo permette di passare il contenuto del documento al modello LLM.

---

# 2. Test

Abbiamo aggiornato il test di `SearchService`.

Il test verifica che una domanda su Python restituisca il documento Python come risultato più rilevante.

Tutti i test sono passati:

```text
tests\test_api.py              .   [ 25%]
tests\test_embeddings.py       ..  [ 75%]
tests\test_search_service.py   .   [100%]
```

Quindi:

* API funzionante
* Embedding funzionanti
* Search funzionante
* SearchResult funzionante

---

# 3. LLM locale

Abbiamo deciso di non utilizzare API a pagamento.

È stato installato **Ollama** e abbiamo utilizzato:

```text
qwen2.5:3b
```

Il modello gira localmente sulla macchina.

Abbiamo creato:

```text
src/ai_brain/llm/service.py
```

con `LLMService`.

Responsabilità:

```text
Prompt
  ↓
LLMService
  ↓
Ollama
  ↓
Qwen 2.5:3b
  ↓
Response
```

Il servizio espone:

```python
generate(prompt)
```

in modo che il resto dell'applicazione non debba conoscere direttamente Ollama.

---

# 4. RAGService

Abbiamo creato:

```text
src/ai_brain/rag/
├── __init__.py
└── service.py
```

Il `RAGService` coordina:

```text
SearchService
      +
LLMService
```

La pipeline implementata è:

```text
Question
    ↓
SearchService
    ↓
Relevant Documents
    ↓
Document.content
    ↓
Context
    ↓
Prompt
    ↓
LLMService
    ↓
Qwen 2.5:3b
    ↓
Answer
```

Il metodo principale è:

```python
answer(question, top_k=3)
```

---

# 5. Come funziona realmente la RAG

Abbiamo chiarito che l'embedding continua ad essere fondamentale nella RAG.

## Indicizzazione

Quando costruiamo la Knowledge Base:

```text
Documenti
    ↓
EmbeddingService
    ↓
Document embeddings
    ↓
knowledge_base.json
```

Gli embedding vengono salvati insieme ai documenti.

Nel nostro caso utilizziamo `all-MiniLM-L6-v2`, che produce embedding di dimensione 384.

## Retrieval

Quando arriva una domanda:

```text
"Come funziona Python?"
        ↓
Embedding della domanda
        ↓
Cosine similarity
        ↓
Confronto con gli embedding salvati
        ↓
Ranking
        ↓
Documenti più rilevanti
```

Questa è la parte **Retrieval** della RAG.

---

# 6. Generation

Dopo aver recuperato i documenti:

```text
SearchResult
    ↓
Document.content
    ↓
Context
```

Il contesto viene inserito nel prompt:

```text
CONTESTO:
[contenuto dei documenti rilevanti]

DOMANDA:
[domanda dell'utente]
```

Questo prompt viene inviato al:

```text
LLMService
    ↓
Ollama
    ↓
Qwen 2.5:3b
```

Il modello genera quindi la risposta.

---

# 7. Esperimento RAG

Abbiamo testato:

```text
"Che cos'è Python?"
```

Il sistema ha recuperato il documento relativo a Python e il modello ha prodotto una risposta coerente con il contesto.

Abbiamo poi fatto un test ancora più importante:

```text
"Qual è la capitale del Giappone?"
```

Il database non contiene informazioni sul Giappone.

Il modello ha risposto sostanzialmente che il contesto non conteneva informazioni sufficienti.

Questo ci ha permesso di verificare il comportamento di grounding del nostro prompt RAG.

---

# 8. Concetto fondamentale imparato

Abbiamo distinto chiaramente i due componenti principali:

```text
RAG
│
├── Retrieval
│     ├── Embedding
│     ├── Cosine similarity
│     └── Document retrieval
│
└── Generation
      └── LLM
```

Una formulazione utile da ricordare:

> Gli embedding e la ricerca trovano cosa dare al modello; l'LLM trasforma quelle informazioni in una risposta.

Quindi il lavoro fatto precedentemente con `SearchService` era già una parte fondamentale della RAG.

La RAG ha semplicemente aggiunto il passaggio:

```text
Document retrieval
      ↓
Context
      ↓
LLM
      ↓
Answer
```

---

# Stato attuale del progetto

La pipeline complessiva è ora:

```text
Markdown Documents
        ↓
DocumentLoader
        ↓
EmbeddingService
        ↓
KnowledgeRepository
        ↓
knowledge_base.json
        ↓
SearchService
        ↓
RAGService
        ↓
LLMService
        ↓
Ollama / Qwen 2.5:3b
        ↓
Answer
```

Abbiamo quindi costruito manualmente una prima **pipeline RAG end-to-end funzionante**.

---

# Cosa NON abbiamo ancora fatto

Per mantenere il progetto semplice non abbiamo ancora introdotto:

* LangChain
* LangGraph
* Vector Database
* API `/ask`
* frontend
* sistemi agentici
* orchestrazione complessa

Sono volutamente rimandati.

---

# Prossimo step

Il prossimo passo sarà esporre la RAG attraverso la nostra API:

```text
POST /ask
      ↓
RAGService
      ↓
SearchService
      ↓
LLMService
      ↓
JSON response
```

Dopo aver verificato che anche l'API funziona, potremo finalmente confrontare la nostra implementazione manuale con **LangChain** e capire concretamente quali problemi risolve e quali astrazioni introduce.

## Milestone raggiunta

**Manual RAG end-to-end: COMPLETATA ✅**

# Recap sessione — LangChain e FAISS

## Obiettivo della sessione

Continuare l'introduzione di **LangChain** nel progetto, senza sostituire subito la nostra implementazione manuale.

L'obiettivo è capire cosa LangChain astragga rispetto a quello che abbiamo già costruito manualmente.

---

## 1. Abbiamo introdotto LangChain

Abbiamo installato:

```powershell
python -m pip install langchain langchain-community
python -m pip install -U langchain-huggingface
pip freeze > requirements.txt
```

Per ora utilizziamo LangChain come **seconda implementazione parallela** del sistema RAG.

La nostra implementazione manuale rimane intatta.

---

## 2. Abbiamo creato l'adapter per gli embeddings

File:

```text
src/ai_brain/rag/langchain_embeddings.py
```

Abbiamo creato:

```python
class LangChainEmbeddingAdapter(Embeddings):
```

Questo adapter permette a LangChain di utilizzare il nostro `EmbeddingService`.

In pratica:

```text
EmbeddingService
       ↓
LangChainEmbeddingAdapter
       ↓
LangChain
```

Abbiamo capito la differenza tra:

* `embed_documents()` → genera embeddings per i documenti
* `embed_query()` → genera l'embedding della query

Non abbiamo quindi duplicato la logica di embedding.

---

## 3. Abbiamo creato LangChainService

File:

```text
src/ai_brain/rag/langchain_service.py
```

Il servizio:

1. carica i documenti con `DocumentLoader`
2. li converte nei `Document` di LangChain
3. aggiunge i metadata:

   * `id`
   * `title`
4. crea un vector store FAISS
5. espone un Retriever

La struttura attuale è:

```text
DocumentLoader
      ↓
LangChain Document
      ↓
Embedding Adapter
      ↓
FAISS Vector Store
      ↓
Retriever
```

---

## 4. Abbiamo avuto un primo errore con FAISS

Inizialmente avevamo creato il vector store senza fornire a FAISS l'oggetto embeddings.

Questo provocava un errore durante la ricerca perché FAISS non sapeva come trasformare la query in un vettore.

Abbiamo quindi capito un concetto importante:

> Il vector store deve sapere come trasformare una nuova query in un embedding.

Abbiamo risolto passando:

```python
embedding=self.embeddings
```

a FAISS.

---

## 5. Abbiamo verificato il Retriever

Con:

```python
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 3
    }
)
```

abbiamo eseguito:

```text
"Come funziona Python?"
```

ottenendo:

```text
Python
Pizza
Java
```

Quindi abbiamo verificato che:

* il vector store funziona
* gli embeddings funzionano
* FAISS funziona
* il Retriever funziona

---

## 6. Abbiamo incontrato il problema del threshold

Abbiamo provato:

```python
search_type="similarity_score_threshold"
```

con una soglia, ad esempio:

```python
score_threshold=0.5
```

e abbiamo ricevuto un warning relativo ai relevance score.

Questo ci ha portato a distinguere due concetti:

### Cosine similarity

Era quella utilizzata dal nostro `SearchService`.

In quel caso:

```text
più alto = più simile
```

### Distanza FAISS

FAISS, nella configurazione attuale, ci sta restituendo una distanza L2.

In questo caso:

```text
più basso = più simile
```

---

## 7. Abbiamo verificato gli score reali di FAISS

Abbiamo eseguito:

```python
results = vector_store.similarity_search_with_score(
    "Come funziona Python?",
    k=3
)
```

ottenendo:

```text
Python 0.82403636
Pizza 1.3111918
Java 1.4546695
```

Questo ci ha permesso di capire definitivamente che stiamo osservando una **distanza**, non una cosine similarity.

Quindi:

```text
Python → 0.824  ← più vicino
Pizza  → 1.311
Java   → 1.455  ← più lontano
```

---

# Concetto importante imparato oggi

Il termine generico "score" può essere fuorviante.

A seconda dello strumento possiamo avere:

```text
Cosine similarity
↑ valore = maggiore similarità

L2 distance
↓ valore = maggiore similarità
```

Non possiamo quindi prendere una soglia come `0.5` dalla nostra implementazione manuale e applicarla automaticamente a FAISS.

Le due metriche devono essere confrontate correttamente.

---

# Stato attuale

La parte LangChain funziona:

```text
DocumentLoader
      ↓
LangChain Documents
      ↓
Embeddings
      ↓
FAISS
      ↓
Retriever
      ↓
Documenti rilevanti
```

Il problema ancora da risolvere è:

> Configurare FAISS/LangChain in modo da utilizzare una metrica coerente con la cosine similarity che abbiamo usato nel nostro `SearchService`.

---

# Prossimo passo

La prossima volta faremo **una sola modifica alla volta**.

Obiettivo:

```text
Embedding
    ↓
normalizzazione
    ↓
FAISS con metrica coerente
    ↓
cosine similarity
    ↓
Retriever
    ↓
score_threshold
```

Dopodiché confronteremo:

```text
SearchService manuale
        VS
LangChain Retriever
```

per capire concretamente cosa LangChain sta facendo al posto nostro.

---

## Nota architetturale

Non eliminiamo ancora il codice manuale.

Il confronto tra:

```text
Manual RAG
```

e

```text
LangChain RAG
```

è parte importante dell'apprendimento del progetto.

Solo dopo aver capito la differenza decideremo cosa mantenere.



## Sessione — Chunking e RAG con LangChain

### Obiettivo della sessione

Integrare il **chunking** nella pipeline RAG e verificare che LangChain possa lavorare sui chunk invece che sui documenti interi.

---

### 1. Chunking manuale

Abbiamo creato:

* `src/ai_brain/documents/chunk_models.py`
* `src/ai_brain/documents/chunker.py`

Il modello `DocumentChunk` contiene:

* `document_id`
* `chunk_id`
* `chunk_index`
* `content`
* `title`

Il `DocumentChunker` divide un documento in parti utilizzando:

```python
chunk_size=500
chunk_overlap=50
```

Abbiamo verificato però un limite dell'approccio manuale basato sul semplice slicing delle stringhe: può spezzare le parole o il contenuto in punti poco naturali.

Esempio:

```text
È molto utilizzato nello sviluppo enterprise
e
```

seguito da:

```text
viluppo enterprise
e nelle applicazioni backend.
```

---

### 2. Chunking con LangChain

Abbiamo introdotto:

```python
RecursiveCharacterTextSplitter
```

tramite il package:

```text
langchain-text-splitters
```

Con:

```python
chunk_size=100
chunk_overlap=20
```

abbiamo ottenuto:

```text
Java              → 2 chunk
Machine Learning  → 3 chunk
Pizza             → 1 chunk
Python            → 2 chunk

Totale            → 8 chunk
```

Il risultato è migliore rispetto allo slicing manuale perché lo splitter cerca di rispettare i confini naturali del testo, come i paragrafi.

Abbiamo creato:

```text
src/ai_brain/rag/langchain_chunker.py
```

con il servizio `LangChainChunker`.

Il servizio utilizza `DocumentLoader` per caricare i documenti e `RecursiveCharacterTextSplitter.create_documents()` per generare i chunk mantenendo i metadata:

```text
document_id
title
```

---

### 3. FAISS sui chunk

Abbiamo modificato `LangChainService` per indicizzare i chunk invece dei documenti originali.

Prima:

```text
4 documenti
    ↓
4 embeddings
    ↓
FAISS
```

Ora:

```text
4 documenti
    ↓
chunking
    ↓
8 chunk
    ↓
8 embeddings
    ↓
FAISS
```

Il metodo principale è ora:

```python
load_chunks()
```

che utilizza `LangChainChunker`.

Il vector store continua a utilizzare:

```python
faiss.IndexFlatIP
```

con embeddings normalizzati, così l'Inner Product corrisponde alla cosine similarity.

Manteniamo inoltre:

```python
relevance_score_fn=lambda score: float(score)
```

per utilizzare direttamente lo score restituito da FAISS come relevance score.

---

### 4. Test del retrieval sui chunk

Abbiamo verificato il comportamento con:

```text
"Come funziona Java?"
```

Risultati:

```text
Java              0.6089
Machine Learning  0.2814
Pizza             0.2300
```

Il chunk Java viene quindi recuperato correttamente come risultato più rilevante.

Questo conferma che il vector store sta effettuando il retrieval a livello di **chunk**.

---

### 5. RAG con chunk

Abbiamo verificato anche il `LangChainRAGService`.

Domanda:

```text
Qual è il ruolo di Java nello sviluppo backend?
```

Risposta:

```text
Java è molto utilizzato nello sviluppo backend.
```

La fonte recuperata è il chunk Java contenente:

```text
È molto utilizzato nello sviluppo enterprise
e nelle applicazioni backend.
```

Il RAG ora utilizza quindi effettivamente il chunk come contesto per il modello.

---

### Pipeline attuale

```text
Markdown documents
        ↓
   DocumentLoader
        ↓
RecursiveCharacterTextSplitter
        ↓
      Chunks
        ↓
Sentence Transformers
(all-MiniLM-L6-v2)
        ↓
      FAISS
        ↓
    Retriever
        ↓
     Context
        ↓
   Ollama / Qwen 2.5 3B
        ↓
      Answer
```

---

### Concetti appresi

In questa fase abbiamo introdotto:

* Text chunking
* Chunk overlap
* Recursive character splitting
* Document retrieval vs chunk retrieval
* Vector Store
* FAISS
* Retriever
* RAG con chunk
* Similarity score
* Limiti del similarity score come indicatore della qualità della risposta

Un punto importante emerso durante il progetto è che:

> **Similarity score ≠ qualità della risposta**

Un chunk può essere semanticamente simile alla domanda ma non contenere necessariamente informazioni sufficienti per rispondere correttamente.

---

### Stato attuale

La pipeline RAG con chunking è funzionante.

Tecnologie principali utilizzate:

```text
Python
Sentence Transformers
NumPy
scikit-learn
FAISS
LangChain
LangChain Text Splitters
Ollama
Qwen 2.5 3B
```

---

### Prossimo step

Il prossimo obiettivo è introdurre una prima forma di **Retrieval Evaluation**.

Vogliamo passare da:

```text
"Il retrieval sembra funzionare."
```

a:

```text
"Possiamo misurare quanto bene funziona."
```

Partiremo da un piccolo dataset di domande con risultati attesi e introdurremo gradualmente:

* Top-K
* Score threshold
* Hit@K
* Precision@K
* Recall@K

L'obiettivo è capire concretamente come valutare e migliorare il componente di retrieval prima di aggiungere ulteriore complessità al sistema.
