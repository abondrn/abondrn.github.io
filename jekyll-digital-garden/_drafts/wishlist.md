---
title: Things I Wish Existed
permalink: /wishlist/
date: 2021-10-14
---

# Introduction

Like a lot of people, I have various side projects in various stages of completion. While originally, these projects were motivated by some notion of being useful to myself or others, I have less and less time to devote to bring these into existence.

Because of this, in the spirit of [working in public](https://blas.com/working-in-public/), I want to draw attention to gaps I see in the market. This is interesting from a purely product standpoint, as I feel like there are many apps that are launched to little fanfare or become vaporware with a solid idea but poor execution.
My hope is that by talking about what I can either gauge interest from others to motivate me to create a product, inspire someone else to make it, or discover it already exists.

In addition to describing the motivation and some MVP features, I elaborate what platforms should be targetted first, how much I think it should cost, along with some populations that might particularly benefit and some potential strategies to attract early adopters from those groups.

# Apps I wish existed

## Community-Oriented Aggregators

### People-Oriented Feeds, Social Intelligence Platform

In the past few years there has been a growing desire for "personal CRM" solutions: software that would help you build deeper relationships. In practice, using one of the currently available apps feels like data entry, and quite unlike what the process of maintaining a friendship should "feel" like. At the same time, the decline of monolithic platforms like Facebook and Twitter means that people are spread more across multiple platforms. Out of a desire of "meeting people where they are," I would like to better keep track of where everyone is.

My solution would be a local-first app. You would connect the few APIs that allow social graph access, and the rest you would feed it data dumps you request from various platforms. With this, you have access to all of your connections (and ideally messages) between you too.

This is where it gets fun. This could be an interesting layer to build applications on top of. You might have a mobile app that might be a "linktree" for various contexts/identities. You can compute various "Venn diagrams" between yourself and your connections. Sort them into groups (circles), and record your interactions. Compute second-degree connections on API-enabled platforms. Be a place where you can share and view others recommendations and referral codes, as well as plan future events together.

This could also be used for people you are not mutual connections with, ie celebrities and role models, potential business connections. Imagine being able to view someone's publications/IMDb, news alerts/interviews, biography, and collaborations publically to find more stuff you might like.

Featurelist
 - business card: share one of your profiles with a single QR code
 - public/private profile curation: share a subset of your services
 - gifts
 - populate a social map from your friends' Instagrams, Yelp reviews
 - scrape mutual follows/likes
 - share referral codes
 - find out whether your contacts are on various services using OSINT tools
 - track hangouts with geotagging, message history
 - share your current location, upcoming travels to coordinate meetups
 - assemble feeds from various platforms (YouTube, Twitter)

### Matching

Tinder is based on a simple concept: you only see eath-others profiles if you both swipe right at each other. I'm not saying there should try to emulate Tinder, but the idea stands: you could replace swiping with other types of commonality.
Swiping also signals something else: you downloaded an app and are actively looking for someone, so you are implicitly weeding out people that don't want to be bothered.

Being a part of a common community is a good starting point, and a good way to onboard people to the concept.

You might be thinking this is like Facebook, or at least what it used to be. "like the pages" of things you're interested in, and get friend suggestions out.

But it needn't stop there. 

Of course, [finding the others](https://www.goodreads.com/quotes/514216-admit-it-you-aren-t-like-them-you-re-not-even-close) would ideally happen organically. But a lot of us aren't lucky enough to bump into a lot of people on a daily basis, especially when you get older.

## Lifelong Learning

Educating the next generation always seemed like one of those wicked problems.

### Microlearning

There could be ample opportunities to learn, but because there are no good tools that do well at all parts of the process, I stick to my existing suboptimal method.

There are three main parts to knowledge acquisition:
 - Exposure
 - Engagement
 - Repetition

We start with exposure, where the material has to be put in front of the learner for the first time. Here, what's most important is presenting the information in the method most accessible to the student, and spreading it out into chunks so they don't get overwhelmed. Next is engagement, where we progressively move up [Bloom's taxonomy](https://en.wikipedia.org/wiki/Bloom's_taxonomy).
Finally, when repeating we revisit old information on a schedule that keeps it fresh.

For the first step, we could imagine surfacing the best content on a particular topic, whether it be in podcast form, online classes, you name it. It's important here to find content which is at the user's level of maturity, as that is where the rate of learning is fastest. I envision something that lays out [optimal learning paths](https://learn-anything.xyz/) for your subject of choice, but where the individual entries are voted on and the most helpful sources move to the top, and allows you to move deeper and broader depending on your comfort at your current level.

The area of engagement is where most learning software falls short. Systems like spaced repetition and a lot of language learning software stops around the level of recognition because it is difficult to create computer-based exercises that are both intellectually involved, easy to evaluate, and relevant to the area of application. That isn't to say recognition isn't important, it's foundational, but it's not enough on its own.
That being said, even this level could be improved by both automatically pulling cards from relevant sources (trivia shows, kindle highlights, textbooks), and seeding decks from other users' collections a la Quizlet. You increase engagement with these snippets by adding text entry, cloze fields, multiple choice generation, reading comprehension questions, and voice input.
For language, consuming as much media as possible in your desired language has proven to be one of the most effective and engaging ways of getting a firm grasp of a language, and many apps have sprung up to target that modality by adding interactions. You can also turn students into readers for other students' assignments, killing the birds of being able to grade complex assignments and developing critical faculties of more competent students with one stone. There are plenty of other ways to add "learn by doing" with collaboration, for example by doing language exchange programs and open ended group projects.

Finally, there must be repetition for the skill to be retained; there is no growth without consistency. Spaced repetition can easily be adapted to prioritize new information while preempting forgetting over long periods of time. Steps can be taken to make revisiting old information more interesting by using formats such as crosswords and mixing domains.

### Study Cohorts

Matching students into cohorts is one of those problems that sounds easier than it is. In grade school, this is done by year: everyone of a certain age gets grouped together into a "class," and are either put into regular or honors depending on how well you place in entrance exams. In high school you are given a set of electives that you can choose between to fulfill a particular requirement, like art, as well as Advanced Placement/IB classes where you can choose to take a "college level" version of a class. In undergraduate, you are given a high level of autonomy in choosing both your general education and major/minor coursework. Graduate coursework is a bit different in that you split your time between graduate seminars, research, and teaching.

There are aspects to admire from each of these systems. One common thing is the balance of depth and breath -- most times you are given the opportunity to specialize in a specific area only after you have demonstrated the capacity to do well across a range of subjects. This is well intentioned in that it prevents you from specializing too early, but this hurts a lot of smart focused individuals (see list of successful high school graduates) who are only good at a select few things, while also placing general knowledge over specialized skills when it should really be the other way around. There are core skills that are necessary in any field -- rhetoric, problem solving, project management, grit -- but the specific subjects can study to attain those is often interchangeable.

It also establishes certain windows in which you are allowed to be a beginner-generalist. Well into high school, you are discouraged from gaining real world professional experience, and for many the end goal seems distant which can drain their motivation. Then, after undergrad, it is often discouraged to start your career over and gain skills in an unrelated area with few exceptions.

In my ideal world: learning would not be compressed in the first 20 years of one's life. It would be project focused, collaborative, and self-direcxted. A student would be assessed for their current level of knowledge and skills in a subject, be matched to their peers in a global pool of students, and be given a schedule that lines up with them. As a student matures, they'll be given increased responsbility to teach the younger classes and do research projects in their chosed specialty, while they enrich their minds in an evolving rotation of additional coursework and extracurriculars.

They start working earlier, but are given points in their lives to do sabaticals if they need an intellectual switch-up and do masters if they show promise in a subject area. Part time research, teaching, and learning should be the norm.

## Interactive Documents for Collective Knowledge Management

## Augmented Audio Assistant, Ambient Agents

Overreliance on screens

Audio as an underutilized medium