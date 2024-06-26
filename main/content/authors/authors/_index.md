---
# Display name
name: Yifan Zhao

# Username (this should match the folder name)
authors:
  - authors

# Is this the primary user of the site?
superuser: true

# Role/position
role: Computer Science Ph.D. Student

# Organizations/Affiliations
organizations:
  - name: Univ. of Illinois, Urbana-Champaign
    url: "https://cs.illinois.edu/"

# Short bio (displayed in user profile at end of posts)
# bio: My research interests include approximate computing, compiler stack for heterogeneous computing, and a mindful blend of both.

interests:
  - Programming Languages
  - Compiler System
  - Approximate Computing

education:
  courses:
    - course: Ph.D. in Computer Science
      institution: University of Illinois at Urbana-Champaign
      year: 2019 - Now
    - course: BSE in Computer Science Engineering
      institution: University of Michigan
      year: 2017 - 2019
    - course: BSE in Electrical and Computer Engineering
      institution: Shanghai Jiao Tong University
      year: 2015 - 2019

# Social/Academic Networking
# For available icons, see: https://sourcethemes.com/academic/docs/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.
social:
  - icon: envelope
    icon_pack: fas
    link: mailto:yifanz16@illinois.edu
  - icon: twitter
    icon_pack: fab
    link: https://twitter.com/evanzhao97
  - icon: github
    icon_pack: fab
    link: https://github.com/Evan-Zhao
  # Link to a PDF of your resume/CV from the About widget.
  # To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
  - icon: cv
    icon_pack: ai
    link: files/cv.pdf

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups: []
---

I am a 5th-year Ph.D. student in the [Department of Computer Science](https://cs.illinois.edu/) at the [University of Illinois Urbana-Champaign](illinois.edu).

I am co-advised by [Prof. Sasa Misailovic](http://misailo.web.engr.illinois.edu/) and [Prof. Vikram S. Adve](https://vikram.cs.illinois.edu/).

My research interest is in compilers and programming systems for tensor programs.
Compilers are an unique vehicle for a myriad of intriguing program optimizations:

- Tensor compilers feature specific optimizations
  [(loop nest optimizations](https://en.wikipedia.org/wiki/Loop_nest_optimization),
  [polyhedral model](https://en.wikipedia.org/wiki/Polytope_model), ...)
  that are highly effective to tensor programs;
- [Accuracy-aware optimizations](https://misailo.web.engr.illinois.edu/papers/misailovic-accuracy-aware-optimization.pdf)
  won't even preserve your program's semantics, but they carefully reason about how much havoc they wreak
  and can be alike beneficial for tensor programs (pruning, quantization).
- Of course general purpose optimizations are not going away: DCE, CSE, LICM, ...

Together they present a tough challenge (and opportunity!) of _choosing the right optimizations to apply_ to a given tensor program.
See my recent projects and [CV](/files/cv.pdf) for more details.
