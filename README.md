# Parsing Hegel


In another life I read a lot of Hegel, now a mere side-interest. Despite the assurances of my former supervisor Bob Stern to the contrary, Georg Wilhelm Friedrich Hegel's work is infamously opaque. Making sense of his *Phenomenology of Spirit* poses a considerable challenge, and those who claim to understand him often end up with rather different readings.

In my current life, I am finishing up an MPhil in Advanced Computer Science. My project is in the area of computational semantics where we seek to make sense of expressions in natural language by automatically producing formal representations of their meaning. For this purpose, I am using the Boxer-parser, which uses Discourse Representation Theory (DRT).[0] DRT offers a fancy formalism for capturing action-sentences using a neo-Davidsonian event semantics. One benefit of this theory is that it allows us to represent the meaning in neat little boxes, hence the namer of the parser. The boxes specify a number of variables at the top and then contain conditions in the form of predicates below.

If computational semantics enables us to make sense of natural language. Then why not use it to make Hegel approachable? Why not run Boxer on the *Phenomenology* I can think of very good reasons to resist the idea, but not of a single one that would keep me from giving it a try with at least one sentence. So I just went ahead and adapted a tiny sliverof  what I have learned during my MPhil to turn the first sentence of the *Phenomenology* into a formal representation.

The challenge should not be underestimated. The first sentence reads as follows:[1]

"It is customary to preface a work with an explanation of the author's aim, why he wrote the book, and the relationship in which he believes it to stand to other earlier or contemporary treatises on the same subject."

This is not exactly "The dog chases the car", an example much more adapted to the powers of Boxer. But I have to admit that Boxer surprised me. It managed to produce a representation of this first sentence:[2]





Despite the intuitive character of the boxes, it is not exactly easy to make sense of the jumble. Boxer seems to have produced to less than complete parses, hence the repetition of certain elements (e.g. "contemporary treatise"), but I am honestly impressed that I got anything at all. 



I want to suggest that Hegel's *Phenomenology* in fact works better with the neo-Davidsonian approach of Boxer than other philosophy texts, because it tries to describes the actions and experiences of spirit. What it describes is closer to action than what we find in most philosophy books. 

If you generously fund me for four to five years, I will try to produce such representations for the whole of the *Phenomenology*. The decision whether that is a worthy investment of your money is up to you.



[0] Kamp, Hans, and Uwe Reyle. *From Discourse to Logic: Introduction to Modeltheoretic Semantics of Natural Language, Formal Logic and Discourse Representation Theory*. Studies in Linguistics and Philosophy 42. Dordrecht: Springer-Science+Business Media, B.V, 1993.

[1] I am using the Miller translation.

[2] The parse neglects a few niceties such as representing the word-senses was WordNet synset and the like, but that is not the problem.
