Hi! If you're reading this, I either sent this to you or you stumbled upon this on my website. If you're not a recruiter, there probably isn't much benefit to you reading this page, but if you are, I encourage you to read this to get a sense of whether or not we would be a good match! 

<!-- One day, I hope to make this interactive so you can "talk" to me as a candidate, but in the meantime, use this as a cover letter for your open role. -->

This is a distillation of much introspection and talks with recruiters over the years. I think it is a better format than a resume since it encapsulates what you want to know, and saves both us time.

## What is my current role/what roles am I looking for?

I am currently a bioinformatics software engineer. I often get questions about what this means, from people who work outside of biotechnology. I like to explain it as an *interdisciplinary role* which does work normally associated with more specialized roles within typical technology companies. To summarize, here is how I would describe it interms of other roles:
1. Backend Software Engineering: Like backend engineers, I create and maintain APIs to perform specialized functions. Typically, these services are *read-only*, in the sense that they accept some data, and then do some combination of performing computation or querying a database, but without altering the underlying data store. I have developed new APIs using eg. FastAPI, and have experience with querying and managing databases.
2. Data Engineering: Like data engineers, I maintain pipelines that process large volumes of data (*"big data"*). This comes in two forms. Either, I create or maintain *pipeline components* which are triggered by availability of upstream data (a patients' sample being sequenced or the completion of an intermediate component), or I perform large-scale analyses which attempt to answer questions using results of previously completed jobs. This involves developing robust ETL pipelines, often written in Python, which use many standard libraries such as Pandas and Polars, as well as some which are specific to bioinformatics. Sometimes, these pipelines are written in DSLs such as Snakemake and Nextflow, and use techniques such as async and parallelism to optimize for performance.
3. DevOps: Like devops engineers, I develop internal developer tools and CI/CD pipelines.
4. Quality Assurance/Test Engineering: Each component must comply to high quality standards because I work in a regulated as well as a high risk field. This means that, in addition to defining the unit and integration tests which are typical in the software field, there must also be more in depth validations which must be performed across the entire system. This includes analyzing data diffs between a pipeline before and after a single component is upgraded, as well as verifications where I work with the clinical science team to ensure the data output is high quality after many runs.
5. Machine Learning Engineering: There is large overlap with the "ML Engineering" at most companies and my above responsibilities. I also have personal experiences training ML models, and have worked on LLM projects both personally and professionally.

### RE: Lacking some skills

I often hear that while I overall show a match to a given role, I don't meet the target candidate profile 100%. This might come in the form of:
 - Not having an advanced degree (Masters/PhD) or publications
 - Not having X *professional* years of experience in Y technology
 - Not having held X title (data science, etc)

These are perfectly valid objections, and your perogative. I prefer to be 100% upfront and honest when I don't meet a particular qualification. But, I would argue that it is better to screen for capabilities: would I be able to *learn* a particular skill.

This has numerous components:
1. Would I be able to acquire this particular skill in the time needed to be productive? I think this is evidenced by numerous things: I have a strong technical degree from a top university, I have acquired many technical skills in the past (sometimes by self-teaching), and I frequently have to acquire skills (programming languages, domain expertise, etc) on the job.
2. Would a candidate with the particular skill sets you are looking for need spin-up time to be productive in your organization? I would argue *yes*, this is universal and unavoidable.
3. The best way to check my fit is by interview or coding assessment.

## What I look for in a team/company?

I don't apply to every role I am qualified for because I believe employee-employer fit is important. For larger companies, I ask these questions of a particular team because one's experience can vary widely within an organization, and thus usually withhold them until the team-matching phase.

### The most important question

As a long term thinker the most important question I ask when I evaluate a new opportunity is, "if I take this role, where will I be in 4 years?" The choice of time period is arbitrary, but it's also an important one. Four years is how long I spent doing my undergrad, around how much time I would spend in a PhD, and how much time I have been at my current role as I am writing this. It's a time period I would like to look back on and be proud of what I have accomplished, for my company, team, and myself. As you'll see, this framing is important as it helps me narrow in on some expectations I would like to see in my next role, and informs my decisions.

#### Where will the company be in 4 years?

Financial forecasting is hard. There's a reason why venture capital is difficult, and the large majority of rewards go to a few firms (*"winner take all"*). Yet, as an engineer, I cannot escape this question. Not only is my employment dependent on whether or not the firm goes bankrupt or decides to do layoffs, but depending on proportion of base vs equity compensation, the choice of company can have a huge impact on my future.

Like it or not, I have to *play venture capitalist* when evaluating new opportunities, because I am staking my career on the decision to join your firm. As a result, I like to ask questions about things like runway, revenue growth, sales/customer acquisition, etc, to help improve the odds of making the *right* choice.

An important aspect of this is the concept of *moats*, or competitive advantage. Because you are unlikely to be in the first in your area, and may be competing against large incumbants, **what sets you apart**? What will allow you to move faster and build better products? Having a concrete answer to this question will make me very excited about joining you. Additionally, I like to ask how the business will be affected by AI? Is it entirely reliant on external APIs to add value(*"GPT wrapper"*), is the core business resiliant to AI progress (*hard tech* or not-entirely-software), or something else?

#### What kind of impact can I have in 4 years?

**Does the team work on a public facing product or produce public artifacts?** In previous roles, I may spend part of my time developing systems or tools internal to a particular company. While this can be gratifying, because you can see the option of it internally and collaborate directly with people who use or interface with your tool, it can also be hard to point to your particular contribution both inside and outside of the company. I like to ask times members of the team have been credited in **research publications** or **patents**, contribute to **open source**, spearhead **features** in generally-available services, speak at **conferences**, develop **industry standards**, etc. Whether these are at the team or individual level, or in a primary or support role, a healthy team provides opportunities to do this.

**What problem is the team trying to solve**? In the process of interviewing, I try to establish how far removed I am, as an employee, to fixing a given problem in the world. For instance in my given role, this means *developing software/systems to process genetic data -> so that generated reports used by clinicians to better inform the standard of care -> so that cancer patients have a better chance of survival*, or **3 steps removed**. For some companies, this might be larger; for others, which function as *middlemen*, they merely facilitate transactions without any indirect impact. How many steps removed is this team? How can you quantify that this team is doing a good job, beyond just *customers* or *revenue*?

**How does my role help the company earn revenue**? A common pattern I see at biotech and pharma companies is once the core *platform* or *research* is done, the team responsible is let go to *"streamline operations"*. In general, it makes me more comfortable knowing that the work I do helps to improve the core product in a *measurable way*. Is there a culture around measuring individual impact and rewarding it?

#### How will I grow and learn in 4 years?

As of writing this, I still consider myself to be a early-mid stage engineer. The decisions I make now determine where I will be in my career as I progress. For example:

**How will the skillset that I develop be affected by AI?** Will I be the run-of-the-mill engineer, performing maintenance or development tasks that will become more commoditized with the growth of AI developer agents? Or do I get to participate in such advances by building on top of the latest technologies, perhaps assisting in the automation?

**Am I developing skills that transfer well to other companies or domains**? While I have enjoyed working in biotech and bioinformatics, I acknowledge a common objection I get, which is that it is not easy to "place me" onto an existing clear-cut mapping of backend developer / data engineer / data scientist etc. For my next role, I am eager to be doing work where I am developing skills that can also transfer to other domains. For instance, am I working with **modalities of data which are common across industries** (image, unstructured text, graph, etc)? As an engineer, I am working with **industry standard tools** or **open source packages**?

**How will my team invest in my growth?** What is the mentorshop culture like on the team? Will I be given latitutde to suggest ideas and work on projects I believe have value (open source or not)? How have other engineers risen up in the organization (and were they hired by internal referral or not)? Is there an education/conference stipend?

### Other considerations

#### Learning vs Earning

I don't have any hard and fast rules for ruling out opportunities. But something I like to keep in mind is what I like to call the *"learning versus earning"* tradeoff.

Top technology and Fortune 500 companies have the most expertise, resources, and funding. This means that they can pay the very top of the band, AND have good benefits (health insurance, 401k matching, you name it). They are also more stable (have a higher probability of surviving the next year) and because their equity is often publically traded it could almost be considered another form of base compensation. They typically also have better work-life balance as they are no longer in "survival mode."

Yet, these same traits make them less likely to move quickly where it counts, and there might be less opportunities to advance. Decision making tends to be more bureaucratic and political. They might be willing to invest in the "cash cow" and even speculative research, but might not be willing to take a chance and go "all in" when it counts. They think in quarters, not in days. Even just given the number of employees, it's harder to make that individual impact.

Bringing it back to what I look for in a role, I try and place where it fits on this spectrum. If it's an "earning" role, I might not be too picky on what I work on if I am making top of band. But if it's a "learning" role, I will be very focused on whether a role aligns with my interests and growth. Being a startup is not enough, there needs to be the right culture and problem to make this work.

#### Company Size

I am not opposed to working at startups. But the smallest company I have worked at thus far is Tempus, and they already had over 1,000 employees when I joined. I am willing to take a risk on smaller companies, if they are also willing to take the risk on me. If a recruiter is reaching out, I like to see that there is an even mix of direct hires (directly brought on by the hiring team/internal referrals) and recruiter hires (like me), so there isn't too much favoritism.

#### Industry

Most of my career has been spent in the biomedical space, but I hope by looking at my prior internships and this page, you can see that I have interests outside of this space too. There are a lot of problems to be solved with data! I viewed genetic testing as one such area when I was recruiting as a new grad, but I see no reason to limit myself to it now, even if I am open to staying for the right opportunity.

#### Project-Based Work

While my time at Tempus has *not* been project based (I am largely supporting existing services, pipelines, even if I am building on them to add new functionality and analyses), I am certainly open to and in some cases might *prefer* project based work. This could mean doing research engineering (building new models), sales engineering (onboarding new customers), consulting, etc. I am also open to remote contracting and part-time work.

#### In-Office Policy and Work Life Balance

If I have one nonnegotiable, it is that I am based in San Francisco and not open to relocation. I also do not drive, which means I am only open to SF or remote roles **only**.

I am flexible with regards to commuting to the office. For companies that are located in San Francisco or have SF shuttles (or generous commuter benefits), I am open to doing 5 days-a-week in-person. For other companies which are located in the Bay Area, I am open to commutting via BART and CalTrain, if there's flexibility on how many days per week or what time I come in. I understand the value of in-person collaboration. But it can be counterproductive to ask people to come in on a daily basis, particularly when the team is distributed, and/or the commute is long.

I don't think that work should *always* be confined to **5 days a week, 9-5**, but this should be the *norm*. On-call rotations are standard. Sometimes, more time is needed to put the finishing touches on a presentation or demo for an important client. Sometimes, businesses are seasonal and might tend to require more hours in one part of the year than an other. But aside from this, I try and ask if the team makes reasonable expectations of its employees, and aims to distribute work so work does not consume their life. Parents on the team are often the best to ask about this. Speaking personally, having time to stay fit and spend time on hobbies **avoids burnout and allows to be as productive as I can be**. Frequently working weekends or late nights *in office* is not conducive to this.

## Other Notes for Recruiters

I have had great interactions with recruiters in the past, and with others not so much. Here are some guidelines if you'd like to work with me.

### Don't ask me to apply

You've already messaged me, get to know me! I can give you whatever information you need over the phone or by email. Likewise, don't expect me to write a cover letter.

### Don't message my work email

I don't reply. You should reach out to abondarenko@berkeley.edu.

### I don't take recruiting calls before 10am PST

For whatever reason, I've seen an uptick in recruiters from the UK. That's fine, but don't be surprised if I don't end up scheduling anything.