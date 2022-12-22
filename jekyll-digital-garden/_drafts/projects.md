---
title: Ongoing Projects
---

# Started

## This Website (Jekyll+JS)

### History

[[***Changelog***<br/>
\- 14-05-20 Context Menu <br/>
\- 08-05-20 Trivial Spaced Repetition <br/>
\- 04-05-20 Removed Theming. <br/>
\- 04-05-20 Removed Curated Notes. <br/>
\- 01-04-20 Curated Notes. <br/>
\- 30-04-20 Transclusion. <br/>
\- 26-04-20 Sidenote. <br/>
\- 20-04-20 Wiki link. <br/>
\- 16-04-20 Theme. <br/>
\- 16-04-20 Avatar. <br/>
\- 11-02-20 Related Posts. <br/>
\- 12-10-19 Searchbar. <br/>
::rmn]]The original design[[**Original Design**<br><img src="/assets/img/firstdesign.jpg">::lsn]] of this website was a lot more ostentatious than what you see here. As I progressed through the development process of this website, the current design started emerging on its own. For reasons I don't even understand, the current design just started feeling more natural than the one I had in my mind initially. The bare and simple look-n-feel of this site, at least to me, encompasses the essence of all the things I love about the sites I frequently visit --- feed-like structure, previews, search with context, contextual backlinks, sidenotes, etc. I am hopeful that you'll love it too. :)

- **Page preview** (Move your mouse over the link): [[Introduction to Simply Jekyll]]
- **Transclusion**: Allows you to see a partial view of the contents of the website to the right or the left of the margin.
- **Sidenotes** (Changelog you see on the left is an example of this).
- **Wiki-style link:** Usually wikis allow you to specify links using double bracket, I added it here using liquid. Also added bad-link highlighting
   - Good link: [[Introduction to Simply Jekyll]]
   - Bad link: [[Title of a page that doesn't exist]]


Some less known features:

- Go back to the blog home or to the notes page, and try to right click on any of the entry. [Hint: Zettelkasten]

- Press 'Shift + s' to trigger search

- Click this card[[Memorize me so that you do well in your exams::srs]] looking thing to know how I use my notes. [Hint: SRS]


Other Details:

- The site lives on [[Github::https://github.com/rgvr/simply-jekyll]] and is served using Netlify
- This website is statically generated using Jekyll from a set of Markdown files.
  - The Jekyll theme can be found on [[Github::https://github.com/rgvr/simply-jekyll]], It is called "Simply-Jekyll"
- Except lunrjs and katex, there are no third party libraries. Discord is an opt-in, I don't use on my [[site::https://rgvr.me]]. I strongly believe in user privacy.

### Planned Features

 - [ ] Glossary
 - [ ] Autoembed
 - [ ] Import notebooks
 - [ ] Better LaTeX support
 - [ ] Level-of-detail eliding
 - [ ] Scrolling TOC
 - [ ] Gitalk comments
 - [X] Gwern style citation, sidenotes
 - [ ] Gwern style content previews and archiving
 - [ ] Comments-as-annotations

### Semantic Ontology Templating

HTML already has native support for definitions, which can be used to create a glossary. This glossary can then be automatically ingested into a Spaced Repetition library. 

The Semantic Web, as a concept has existed for a long time. SW resolves around the use of RDF tuples to represent entities and their relationships. One project that serves as a good example of integrating Semantic concepts into an existing wiki is the Semantic MediaWiki extension.

### Interactive, Data-Driven, Dynamic Documents

Information can "come alive" with the use of reactive visualization. For example, with the use of timelines, maps, networks, and other charts. See Explorable Explanations for this implemented in practice, as well as R Shiny Dashboards.

## Music Score Browser (Python)

I modified an existing web app to help me with doing harmony assignments for my Music Theory class. I would like to modify the existing functionality to do the following:

 - scape a library of open source MIDI music, convert them to interactive sheet music
 - using source separation models, create a MIDI scores for popular songs
 - use models to add dynamic accompaniment and harmonization for infinite improvization
 - rate the difficulty of pieces and allow students to find appropriately challenging pieces to their current level
 - use music generation models to offer a "diffusion editor" experience

## Career Helper (Python)

I created a templating tool which automatically generates a web/PDF website based on a YAML document specifying my qualifications. On top of this foundation, I plan to build the following capabilities:

 - edit LinkedIn profile with up-to-date information via the API
 - scrape job board descriptions, build a Notion or Airtable database annotated with the Glassdoor API, levels.fyi, Crunchbase
 - score your resume against a job description, aggregate top skills to learn and find relevant courses
 - GPT-powered cover letter writing

## Spotify Music Tagger (Python)

In the past, I have build a random forest classifier to sort my Liked Songs into playlists, since Spotify lacks a lot of features in the way of organization despite having a lot of information available for free via the API.

Next steps:
 - make it easy to listen to the recommended songs for each playlist, and either add or skip
 - classify songs by emotion so you can listen to songs that match your mood
 - DJ: make a playlist seeded with an initial song and creates a smooth gradient to other songs of choice
   - download the songs and make a podcast which makes seamless transitions between each song in the playlist
   - Spotify previously had a feature to create a running playlist. Enter details about your run and your target pace and it should spit out an appropriate playlist.
   - add visualization via music video, GIFs, or GLSL shaders

## Quantified Self (Python)

Coming around December 2022.

## Discord Bot (Kotlin)

## Productivity (Flutter)

I have gone through many productivity systems in the past, and I believe you can get a lot of mileage by leaning hard on two features: a **duration estimate** field and **outlining**. This is because it encourages to reduce projects and goals down to their atomic components; when an objective is a composition of these atomic steps, it is most of the way to becoming [SMART](https://en.wikipedia.org/wiki/SMART_criteria) and becomes a lot more "real" in a way that inspires you to make the rest of the journey there. There are plenty of task managers that handle one of these well, as there is no dearth in either outliners with due dates or incorporate pomodoro timers as a key concept, some but I haven't found one yet that combines both effectively.

A time metaphor is particularly apt. There are only 24 hours in a day and a typical person can only spend so much time being productive in a way, which presents a natural cutoff for realistic daily plan, and you can get most of the benefits of calendar time blocking without locking yourself into a [manager's schedule](https://fs.blog/2017/12/maker-vs-manager/). Salaried and freelance workers have an intuitive grasp of the money-time trade-off, and would benefit from seeing their past and future activities in such terms. Aggregating statistics of the actual amount of time time it takes to complete a particular type of task (i.e., a particular kind of verb), you can begin to estimate similar kinds of tasks more accurately in the future. Mastering a skill is said to take [10,000 hours](https://en.wikipedia.org/wiki/10,000_Hours_(disambiguation)) of deliberate practice, so you could imagine creating a self-guided roadmap to get good at any kind of skill.

I think where most productivity software falls short is forcing you to conform to a particular kind of workflow, ultimately making you spend more time on adjusting to the system than actually getting things done. As nice as organizational features like tags, importance, priorities, effort, contexts... are, I tend to believe that they are more trouble than they are worth, are quickly outdated by new information. Furthermore, by relying to much on GUI elements, these apps choose an interface that "looks nice" but slows down navigation, entry, and editing.

# Ideation

## GIS+AR: geosocial augmented audiovisual exploration + trip planning (Swift)

While cheesy, I enjoy audio tours as a way to better experience museums and road trips. At its' core, this involves playing narration when the user passes certain waypoints. It's a simple concept, but apps I have used in the past will not keep track of which places have been visited so it gets annoying when you follow a nonlinear path (explore).

There are a lot of apps that handle one aspect of the travel planning experience well, but none that tackle all of them and none that make exploration fun with AR.

Featurelist
 - Make multiday trip planning fun with optimization
 - No-car navigation: minimize cost+time for trains, bikeshare, and rideshare modalities
   - Notify when to leave so you don't miss the last train
 - Use AR to label the skyline, mountains, and hiking markers
   - compare sizes of other monuments or mountains
 - Social pinning: view your friends suggestions from Google Maps and Yelp
   - Create custom tours of the city by adding voice note pins; record AV memories
   - Treasure hunts
 - View virtual battle reenactments
 - Overlay historic photos
 - Browse active exhibits
 - Planets and constellations

## Remembrance Agent

Index notes, highlights, saved links, and feeds by storing embeddings in a vector database, then retrieve related content to what is currently on screen.

## Ontology Curation

I would love to gain experience with data fabrics, and it would be really cool to gleam insights from massive networks of interrelated concepts. Once you have the data infrastructure in place, you can impute relations.

 - Biology
   - drugs: adverse events
   - diseases
   - proteins
   - brain regions
   - function
   - metabolic pathways
   - genetic variants
 - History: If we do not study the past we are doomed to repeat it. Applications are broad from improving archival systems, better discover with GIS models, and numerous "digital humanities" projects.
   - ancient texts
   - artifacts, fossils
   - historical borders
   - trade networks
   - etymology
   - estimated economic time series
   - GDELT
   - geneology
   - academic lineages
   - innovations, artworks
   - ancient DNA of early humans, viruses
 - Media
   - tropes
   - box office stats
   - oscar awards
   - color palettes
   - music

In the future I will flesh this out with an analysis of (1) which datasets I can use for the above (2) methods of record linkage, deduplication, and annotation, and (3) cloud platforms or home storage solutions.

## Programming Languages and Environments

Bringing a new language into the world, when there are so many that already exist, seems like a hard bargain. To justify its existence, a new language has to bring the following things to the table:
 - an improved UI/UX: IDE support, compile times (which enable a more iterative development style), package management, a well documented standard library. With the next generation of Copilot-inspired code assistants, the gulf between popular and obscure languages will grow wider still.
 - integrate well with an existing ecosystem, or do something so well that is not possible with a current one: a language can get an early bump in usability simply by piggybacking on an existing language runtime (JVM, JS). This introduces its own set of challenges, namely improving on the limitation of the previous platform while keeping overhead low and providing tools to handle the cases where the runtime leaks through. Even if one adds C-style FFI, integrating with already written libraries and frameworks needs to be less painful than the alternative, particularly when so much of the code written must run on the web or mobile.
 - introduce a new set of contraints. As developers we are often concerned with what our languages *can* do, but often the most innovation in modern languages comes from what you can't do: a stricter type system, simplicity (as opposed to TIMTOWTDI), or forcing adherence to a particular programming methodology (pure functional, prototypical OO, procedural, etc).

With that in mind, here are some programming language concepts I believe there is enough of a gap around to justify a future project to build. For each, the core ideas were refined by unifying existing DSLs or features that exist across several languages packaged under a well-designed syntax.

### common devtooling

 - Codepilot assistant utilizing type hints and docstrings
 - Language server: linter, robust parser, static analyzer, completions
 - VS code syntax highlighter
 - documentation generator
 - REPL, debugger, Jupyter kernel
 - package manager, hoogle search engine
 - graph visualizer
 - profiler

### speaker

 - implementation language: Erlang
 - smart contracts, zero-knowledge proofs
 - Functional reactive programming (working with streams of events)
 - temporal logic (process calculus)
 - interactive fiction
 - general game description language
 - distrubuted data structures: Merkle tree, Kademlia

### plumber

 - implementation language: Python+Rust bindings (embedded)
 - query, inferred types
 - core.spec
 - vectorized parallelism, point free, expressed based, self optimizing
 - pattern matching multimethods
 - embedded, Pandas
 - operator overloading, labels
 - inspectable
 - logic, declarative parsing grammars
 - typing of: exceptions, side effects

### sculptor

 - implementation language: Rust
 - shell script
 - build tool
 - workflow engine
 - distributed
 - streams
 - state machines
