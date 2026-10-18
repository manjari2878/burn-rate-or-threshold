# IEEE WIE Speaker Notes

**Talk:** Zero-Downtime Mindset: Lessons from Moving Mission-Critical Systems to the Cloud  
**Event:** IEEE Women in Engineering Speaker Series 2026  
**Speaker:** Manjari Mettu  
**Length:** 45 minutes presenting + 15 minutes questions  
**Your slot:** tomorrow, 4:00 p.m. MST (7:00 p.m. ET)

Use this as a speaking script, not a paper. For each slide: read the **Say this** section out loud once tonight. If a heading does not match your deck, jump to the slide with the same topic — the order follows the published IEEE session outline.

Do not discuss payment products, payment rails, card/ACH flows, dollar volumes, or customer-account details. Keep every example at the level of **mission-critical production systems** and **customer-facing platforms**.

IEEE WIE asks for educational, vendor-neutral content. Name your employer only on the last slide. Keep camera on. Audience is mixed: students and working engineers worldwide. Teach the idea first, then the tool.

---

## How to use this in the time you have

Tonight (45–60 minutes):

1. Read the **one-sentence job of each slide** in the timing table below.
2. Out loud, practice **Slide 1, Slide 2, Slide 3**, then **Slide 21 and 22**. Openings and closings are what people remember.
3. Pick **one story** for cutover and **one story** for people/on-call. You only need two.

Tomorrow, 30 minutes before you join:

- Water, notes printed or on a second screen, phone on silent.
- Title slide up before you are admitted so you look ready.
- First 20 seconds memorized. After that, talk to the bullets, do not read them.

If you run long, skip **Slide 7** and shorten **Slide 16**. Never skip the close.

Speaking pace: about 2 minutes per slide on average. Title and section-break slides are 30–45 seconds. Teaching slides are 2.5–3.5 minutes.

---

## 45-minute timing map

| Minutes | Slides | Job of this block |
|---|---|---|
| 0:00–4:00 | 1–3 | Land who you are, why this room should care, what they will leave with |
| 4:00–10:00 | 4–6 | Define the zero-downtime mindset and the migration problem |
| 10:00–24:00 | 7–12 | Four engineering moves: phased cutover, rollback, parallel run, data safety |
| 24:00–32:00 | 13–15 | SLOs, error budgets, observability, go / no-go |
| 32:00–40:00 | 16–19 | People: on-call health, follow-the-sun, postmortems, trust |
| 40:00–45:00 | 20–22 | Roadmap, takeaways, invite questions |
| 45:00–60:00 | 23 | Questions |

If the host introduces you, skip repeating your full bio on Slide 2. Say one sentence and go.

---

## Slide 1 — Title

**On the slide:** talk title, your name, IEEE WIE.

**Time:** 30–45 seconds.

**Say this:**

Good afternoon, and thank you IEEE Women in Engineering for having me. My name is Manjari Mettu. I lead Site Reliability Engineering for a globally distributed team across the United States, the United Kingdom, and India.

The title of this talk is Zero-Downtime Mindset. I want to start with an honest sentence: zero downtime is not a slogan, and it is not a tool you buy. It is a way of making decisions when the cost of being wrong is a customer who cannot complete something important.

For the next 45 minutes I will share what actually worked when we moved mission-critical platforms from on-premises infrastructure to the cloud — AWS and OpenShift — without betting the customer experience on a single night of cutover. Then we will have 15 minutes for your questions.

I am glad you are here. If you are a student, this is a map of the work. If you already run production, I hope you leave with language you can use in your next go / no-go meeting.

**Delivery:** Smile. Look at the camera, not the title. Do not apologize for this being your first IEEE talk. Pause after “way of making decisions.” That pause makes you sound sure.

**Transition:** “Let me quickly tell you who is talking, and then we will get into the work.”

---

## Slide 2 — About me

**On the slide:** name, SRE Manager, 13 years in IT, cloud migration, observability, global team, certifications at a high level.

**Time:** 60–90 seconds.

**Say this:**

I have spent 13 years in industry. The through-line is not a particular product. It is this question: how do we change a live system without surprising the people who depend on it?

Today I manage SRE. In plain language, Site Reliability Engineering is the practice of using software engineering to keep production systems healthy — availability, latency, change safety, and the human system around the pager.

My team sits in three regions. That matters for this talk, because reliability is not only dashboards. It is who is awake, who has context, and whether we trust each other at 2 a.m.

I have worked through reliability-driven migration from on-premises environments to AWS and OpenShift, and through building the observability that lets a team say “go” or “stop” with data instead of with hope.

I hold certifications across cloud, Kubernetes, Terraform, and newer AI tooling. I mention that only to say: credentials help you start. Production teaches you what to believe.

**Do not say:** internal org charts, product names, anything about payments, or a long list of certificate names. One sentence on credentials is enough.

**If the host already read your bio:** “You have my background. The only thing I will add is that everything today comes from production, not from a textbook.”

**Transition:** “Here is what I want you to walk out with.”

---

## Slide 3 — What you will leave with

**On the slide:** three or four outcomes. Keep it a promise, not a table of contents.

**Time:** 60 seconds.

**Say this:**

If you remember only three things, remember these.

One: a high-stakes migration is a reliability problem before it is a cloud problem. If you treat it as a project plan, you will optimize for the date. If you treat it as reliability work, you will optimize for the customer.

Two: you can make cutover decisions with Service Level Objectives, error budgets, and observability. Go / no-go should not be a feeling in a war room.

Three: the human system is part of the architecture. On-call health, follow-the-sun handoffs, blameless postmortems, and trust with development teams are how zero downtime survives after the migration banners come down.

I will walk a practical sequence: how we moved traffic in phases, how we planned rollback before we needed it, how we ran old and new side by side, how we moved data without silent loss, how we used SLOs during the cut, and how we protected the people who carry the pager.

Take what fits your environment. Leave what does not. I would rather you steal one practice this week than remember every acronym.

**Transition:** “So what is a zero-downtime mindset, really?”

---

## Slide 4 — Why this mindset exists

**On the slide:** downtime is not an IT inconvenience; it is a broken promise to a person.

**Time:** 2 minutes.

**Say this:**

When a consumer platform is down, we in engineering feel it as an incident. The customer feels it as: I cannot finish what I came to do.

That is why this work is emotional, even when the slides look technical. A checkout that fails, a record that does not save, a request that times out — those are not abstract error rates. They are people waiting.

In mission-critical systems, downtime also stops the business. Revenue pauses. Operations pause. Support queues explode. Leadership asks, reasonably, “Are we safe to keep going?”

A zero-downtime mindset starts with one design constraint: **the customer should not have to participate in our migration.**

That constraint changes everything. You stop asking “When can we switch it on?” You start asking “What would have to be true for the customer to notice nothing?”

Notice I did not say “we will never have an error.” That is not a serious engineering statement. Hardware fails. Dependencies fail. Humans make changes. The mindset is: failure is expected, customer impact is designed down, and recovery is rehearsed.

If you work on a campus system, a hospital integration, a telecom network, a public cloud control plane — the same constraint applies. The domain changes. The duty does not.

**Transition:** “Let me make ‘zero downtime’ concrete, because the phrase is often used loosely.”

---

## Slide 5 — What zero downtime actually means

**On the slide:** availability as a budget; 99.9% vs 99.99%; zero downtime means designed change, not magic.

**Time:** 2.5 minutes.

**Say this:**

Engineers love nines. 99.9 percent availability is about 43 minutes of unavailability in a 30-day month. 99.99 percent is about 4 minutes. Those numbers are not decorations. They are a budget for how much the world is allowed to break.

Zero downtime, in practice, means three things.

First, **unplanned customer impact is rare**, and when it happens it is short.

Second, **planned change is invisible**. Upgrades, failovers, and migrations happen behind a traffic shift, not behind a maintenance banner if we can avoid one.

Third, **we can reverse**. If the new path is wrong, we go back before the customer writes the outage for us on social media.

This is why a big-bang cutover on a Sunday night is the opposite of a zero-downtime mindset. You are concentrating all of the risk into one irreversible moment, with tired people, and with no customer-sized proof that the new world works.

The alternative is slower in calendar time and faster in learning. You move a little traffic. You watch. You compare. You keep a door behind you. You only widen the door when the data says the floor is solid.

I will show you that pattern in the next section. Before that, you need the setting: what we were actually moving.

**If you need a board-friendly line:** “Availability is a promise with math behind it. Zero downtime is how we keep that promise while we change the factory.”

**Transition:** “Here is the migration in one picture.”

---

## Slide 6 — The migration we had to survive

**On the slide:** on-premises to AWS and OpenShift; live production; cannot pause the business; many teams.

**Time:** 2 minutes.

**Say this:**

The shape of the problem was familiar to anyone who has inherited a successful platform.

Years of on-premises infrastructure. It worked. People trusted it. The operational knowledge lived in runbooks and in human heads. Then the business needed cloud: elasticity, faster provisioning, better alignment with how we already ship software.

We were not moving a blog. We were moving systems that had to stay up while we moved them. There was no quiet season where we could turn the lights off.

Two landing zones mattered in our world: AWS for cloud infrastructure, and OpenShift for how we run containers and platform services. I will not turn this into a product comparison. The lesson is independent of brand: **you are changing the runtime, the network path, the identity model, the observability, and the operational muscle memory at the same time.**

That is why “lift and shift, then fix it later” is so tempting and so dangerous. Later is when the old experts have left the old platform, and the new platform still has sharp edges.

My role was reliability operations through that change: how we watch, how we decide, how we recover, and how a global team stays sane.

If you take nothing else from this slide, take this: **migration risk is highest not on the day you copy the code, but on the day you copy the traffic.**

**Do not say:** account IDs, cluster names, vendor scorecards, payment-specific topology.

**Transition:** “So what fails if you treat this as a weekend project?”

---

## Slide 7 — Why big-bang cutovers fail

**On the slide:** unknown unknowns, no rollback window, tired operators, first production is the first real test.

**Time:** 2 minutes. Skip this slide if you are already behind.

**Say this:**

I have never seen a large cutover fail for one reason. They fail for a pile of small reasons that only appear together in production.

The new path has a timeout that was fine in test and fatal at peak. A certificate is wrong in one region. A feature flag defaults the wrong way. DNS cache holds an old answer. A batch job still writes to the old datastore. Monitoring is green because it is still watching the old system.

If your first production users are 100 percent of users, you will learn all of that in public.

There is also a human failure mode. Big-bang cutovers are often scheduled at night “because traffic is lower.” Traffic is lower. Judgment is also lower. The people who designed the system have been in a war room for ten hours. That is not when you want an irreversible decision.

The zero-downtime alternative is almost boring on purpose: small batches of risk, production evidence, a practiced reverse gear.

**A line that lands with students:** “Your staging environment is a hypothesis. Production is the experiment. Do not run the experiment on everybody.”

**Transition:** “Here are the four engineering moves we used, in the order I would teach them to a new lead.”

---

## Slide 8 — Four moves that keep customers safe

**On the slide:** 1. Phased cutover  2. Rollback first  3. Parallel run  4. Zero-loss data movement. Maybe a simple four-box diagram.

**Time:** 45–60 seconds. This is a map, not a lecture.

**Say this:**

Everything else in the technical half of this talk is a variation of four moves.

**Phased cutover** — move a little traffic, then more, then all of it.

**Rollback planning** — write the reverse path before you need it, and test that it actually works.

**Parallel run** — old and new operate together long enough to compare behavior, not just to ping a health check.

**Zero-loss data movement** — if state can diverge, customers will feel it even when both systems are “up.”

None of these is glamorous. Together they turn a cliff into a staircase.

I will spend a few minutes on each, with the decision you are actually making as a lead, not with a tool list.

**Transition:** “Phased cutover first, because it is the one people think they are doing when they are not.”

---

## Slide 9 — Phased cutover

**On the slide:** 1 percent, 10 percent, 50 percent, 100 percent; success criteria at each gate; who can halt.

**Time:** 3.5 minutes. This is a core teaching slide. Do not rush it.

**Say this:**

A phased cutover means the new system earns the right to more traffic.

A pattern that works in a lot of environments looks like this.

Start with internal traffic, or a synthetic journey that exercises the real path. Then a tiny slice of real customers — 1 percent is a common first number, but the right number is: **small enough that a bad hour is recoverable, large enough that you will see real behavior.**

Then 10 percent. Then a region, or a product surface, or a cohort. Then 50. Then 100.

The mistake is treating the percentages as a schedule. “Friday we will be at 50 percent because the project plan says so.” No. Each step has a gate.

At each gate I want three green lights.

One: **customer experience is holding** — success rate, latency, and the handful of user journeys that actually matter.

Two: **the new system is not quietly compensating** — retries, thread pools, and downstream timeouts can hide a bad design until the next doubling of traffic.

Three: **the team can still reverse** — if rollback has expired because data has moved too far, you are not in a phase. You are in a trap.

Name a person who can halt the next phase without a committee. If stopping requires six directors on a call, you will not stop in time.

When I teach this to newer engineers I say: **widening traffic is a production change, not a ceremony.** It gets a checklist, a watch window, and a voice that is allowed to say no.

**Optional 20-second story:** “The best cutover I have been part of looked uneventful from the outside. That was the point. The drama had already happened in the 1 percent and the 10 percent, where only a few customers would have felt it — and we fixed it before we invited everyone else.”

**Transition:** “Phases only work if reverse is real. That is rollback.”

---

## Slide 10 — Rollback is a feature

**On the slide:** rollback criteria, rollback owner, time box, data implications, rehearse it.

**Time:** 3 minutes.

**Say this:**

If you cannot go back, you do not have a cutover plan. You have a hope.

Rollback is not “we will figure it out if something goes wrong.” It is a designed path: traffic returns to the previous good system, within a time you have already measured, with data still consistent enough that customers do not see duplicates, gaps, or ghost state.

Three questions I ask in every review.

**What is the trigger?** Not “it feels bad.” A trigger sounds like: error ratio above this SLO for this many minutes, or a golden journey failing, or a safety alarm we already trust.

**Who turns the key?** One role, with backup. In a noisy war room, consensus is too slow.

**What does rollback not undo?** This is the adult question. If writes have already landed in the new datastore, reversing traffic is not the same as reversing history. You must know, before the night, which data is dual-written, which data is frozen, and which data would need a repair job.

Then you rehearse. A rollback you have never practiced will surprise you. Practice in a lower environment. Practice the communication path. Practice the DNS or flag or weight change you will actually use.

I tell leads: **spend as much design time on the way back as on the way forward.** It feels like delay. It is how you sleep.

**A sentence for the IEEE audience:** “Courage in production is not pushing forward. Courage is being willing to look conservative when the data is not with you.”

**Transition:** “The safest way to learn that the new world matches the old one is to run both.”

---

## Slide 11 — Run old and new in parallel

**On the slide:** dual running; compare results; shadow traffic; only then shift customers.

**Time:** 3.5 minutes.

**Say this:**

Parallel run means the legacy system and the cloud system are both alive, on purpose, for a defined period.

There are a few flavors. You can choose one. You do not need all of them.

**Shadow traffic:** the new system receives a copy of real requests, or a replay, and we compare outputs. Customers still get the old answer. This is how you find “it works in test” bugs without billing the customer for your education.

**Dual serving:** a slice of customers is on the new path, the rest stay on the old path. You already heard this as phased cutover. Parallel run is the operating model underneath it: two stacks, one product promise.

**Dual writes or mirrored state:** when the system stores something the customer will come back for — a record, a preference, a workflow — both sides must agree, or you will “cut over” and then spend months repairing trust.

What you are looking for in a parallel run is not “CPU is fine.” You are looking for **behavioral equality on the journeys that matter.** Same success, same order of side effects, same edge cases.

This is unglamorous work. It produces spreadsheets, diff tools, and arguments about which mismatch is acceptable. Those arguments are cheaper before 100 percent cutover than after.

Set an end date for dual running, or it becomes a lifestyle. Dual running costs money and cognitive load. It is a bridge. Burn the bridge after you have walked across, not while people are still on it.

**For students:** this is the scientific method. Keep the control group. Change one variable. Measure. Then change the next.

**Transition:** “None of this matters if the data arrives incomplete. That is the quietest way to fail a migration.”

---

## Slide 12 — Move data without silent loss

**On the slide:** copy, verify, cut; checksums / row counts / business reconciliations; never trust a green job.

**Time:** 3 minutes.

**Say this:**

I want to be careful on this slide, because data is where migrations look successful and are not.

A copy job that finished is not proof. “Row counts match” is a start, not a finish. Customers do not experience row counts. They experience: is my thing here, is it the latest version, and did anything happen twice?

A pattern that has saved us:

**Inventory what must not be wrong.** Not every table is equal. Identify the records that, if wrong, create a support incident or a safety issue.

**Copy, then independently verify.** Different team, different query, different checksum. If the same script that copied the data also “proves” the data, you have one bug in two places.

**Watch the live stream, not only the backfill.** Most modern systems keep changing while you copy them. You need a story for the tail: how do the last minutes of change get to the new side before you flip?

**Reconcile after cut, on a clock.** For a defined window, compare old and new. Put a human on exceptions. Silent drift is worse than a loud failed job.

I will not walk through vendor features. The principle is: **data movement is a reliability feature with an SLO.** Treat a missed record like an availability incident, because for that customer it is.

**Do not say:** schemas, table names, volumes, anything that sounds like a specific product.

**Transition:** “So far this has been mechanics. Now I want to show you the instrument panel we used to decide go or no-go.”

---

## Slide 13 — SLOs: a promise you can measure

**On the slide:** SLI vs SLO vs SLA, in one plain sentence each; pick a few user-centric indicators.

**Time:** 2.5–3 minutes. Slow down. Many people in this audience have heard the acronyms and never had them explained kindly.

**Say this:**

If you remember one definition, remember this.

An **SLI**, a Service Level Indicator, is a measurement of something the user feels. Availability of a request. Time to complete a journey. Freshness of data.

An **SLO**, a Service Level Objective, is the target we set on that measurement. For example: 99.9 percent of these requests succeed over 30 days.

An **SLA**, a Service Level Agreement, is what you put in a contract. Engineers should not manage to the contract first. Engineers should manage to the SLO, which is stricter and closer to the user.

Why this belongs in a migration talk: during cutover, opinions get loud. The new stack “looks fine.” A dashboard is green. A leader is impatient. An SLO is how you answer, without drama: **are users getting the promise or not?**

Good SLIs for a cutover are user journeys, not CPU. Can the customer start, complete, and confirm the thing they came for? How long did it take? Did we return the correct result?

Pick a small set. Five golden SLIs beat fifty charts that nobody trusts.

Write them down before the night. If you invent the definition of “healthy” during the cutover, you will define healthy as “please let us keep going.”

**A teaching line:** “If you cannot name the SLO, you are not ready to move traffic. You are ready to move hope.”

**Transition:** “SLOs give you a target. Error budgets tell you how much room you have.”

---

## Slide 14 — Error budgets and the go / no-go

**On the slide:** error budget = 100% minus SLO; spend it on change, or save it; burn rate; halt rules.

**Time:** 3 minutes. Core of “data-driven go / no-go.”

**Say this:**

If your SLO is 99.9 percent, your error budget is 0.1 percent. That small slice is not failure. It is the room you have for change, for incidents, for learning.

This is one of the most useful ideas Google’s SRE community gave the rest of us, and it is practical, not ideological.

Before cutover, look at the budget you have left in the current window. If you have already spent most of it on last week’s incident, this is a bad week to take a large risk. That is not fear. That is arithmetic.

During cutover, watch **burn rate**: how fast you are spending the remaining budget. A short spike can be acceptable. A leak that will exhaust the month in a day is not a “wait and see.” It is a stop.

This is how go / no-go becomes a meeting with evidence.

**Go** if golden journeys are inside SLO, burn rate is not eating the month, rollback is still valid, and the on-call team is actually staffed.

**No-go** if you are already burning too fast, if you cannot explain a mismatch, if rollback is compromised, or if the people in the room are too tired to see straight.

I have been in rooms where no-go felt like disappointing people. I now treat no-go as a reliability win. You protected the customer from our calendar.

If you lead engineers, say this out loud before the night: **no-go is an approved outcome.** Otherwise someone will push to 100 percent to protect a date.

**Transition:** “None of those numbers exist without observability. Let me show you what to instrument before, during, and after.”

---

## Slide 15 — Observability before, during, and after

**On the slide:** three columns — before / during / after; metrics, logs, traces, user journeys, alerting that pages on symptoms.

**Time:** 3 minutes.

**Say this:**

Observability is not “we have a dashboard.” It is the ability to ask a new question about production and get an answer without a new deploy.

**Before cutover,** I want the old system and the new system to tell the same story in the same language. If legacy is in one tool and cloud is in another, and the golden journey is only measured on one side, you will argue about reality while customers wait.

Before, you also need **baseline**. What does a normal Tuesday look like? If you do not know normal, every graph during cutover looks like an incident.

**During cutover,** watch a short list on a single screen: the SLIs, the traffic split, saturation of the new side, error types, and rollback readiness. This is not the time to browse. Put a dedicated observer on the board whose only job is to narrate what is true.

Alert on **symptoms users feel**, not on every CPU wiggle. A page that says “the create journey is failing” is a gift. A page that says “pod restarted” is homework.

**After cutover,** do not tear down the old observability on Monday. Keep comparing for a defined period. Some failures are slow: memory leaks, data drift, a batch job that runs weekly. After is where you catch the problems that were too polite to show up on the night.

One more thing, because this audience includes future leads: **if a chart cannot change a decision, it is decoration.** Cutover dashboards should be ruthless.

**If asked about tools:** “The brand matters less than coverage of the user journey, a shared definition of error, and an on-call path that pages a human with context.” Stay vendor-neutral.

**Transition:** “That is the machine. Now the part that actually determines whether this is sustainable: people.”

---

## Slide 16 — Reliability is a human system

**On the slide:** section break. Maybe one line: systems don’t page people; we design the life around the pager.

**Time:** 30–45 seconds.

**Say this:**

Everything I have described will still fail if the team is exhausted, blamed, or working in a different timezone from the incident.

The last part of this talk is the part I care about most as a manager, and the part IEEE WIE audiences often tell me they needed and did not get in a purely technical class.

We are going to talk about on-call health, follow-the-sun operations, blameless postmortems, and trust with development teams.

If you are a student, this is leadership. If you already manage, this is the work.

**Transition:** “On-call first, because a migration that burns out the team is a delayed outage.”

---

## Slide 17 — On-call health

**On the slide:** pages should be rare and actionable; no heroics as a process; sleep is a reliability control.

**Time:** 2.5 minutes.

**Say this:**

A zero-downtime platform with a destroyed on-call rotation is not a success. It is a countdown.

Healthy on-call has a few non-negotiables.

**Pages are rare.** If the phone goes off for things that can wait until morning, people will start ignoring the phone. Then they will miss the page that mattered. Noise is a safety bug.

**Pages are actionable.** The person who woke up should be able to see what is broken, who is affected, and what the first two steps are. A blank dashboard at 3 a.m. is how you create accidental heroes.

**Load is shared.** The same two experts cannot be the plan. If only three people can land a rollback, those three people are now a single point of failure. Document. Pair. Rotate. Teach.

**Rest after the incident is part of the incident.** If someone ran a cutover until 4 a.m., they are not in the 9 a.m. standup as if nothing happened. Fatigue causes the next event.

During a migration, on-call gets worse unless you plan the opposite: extra coverage on phase days, a clearly staffed war room, a quiet period after 100 percent for the people who carried it.

I say this especially to women and to anyone who has been told that being always-available is how you prove you belong. **Belonging is not measured in hours awake.** Belonging is measured in whether the system is designed so a human can do excellent work and still have a life.

**Transition:** “My team is in the US, the UK, and India. That can either save us, or it can mean someone is always paying the night-shift tax. Follow-the-sun is how we choose the first.”

---

## Slide 18 — Follow-the-sun without dropping context

**On the slide:** US / UK / India; handoff checklist; one source of truth; no “we will tell them tomorrow.”

**Time:** 2.5 minutes.

**Say this:**

Follow-the-sun means the pager and the incident live in the timezone where people are supposed to be awake.

It sounds obvious. It fails in the handoff.

A bad handoff is: a chat message that says “all good, watch X,” and the next region spends an hour reconstructing what X was.

A good handoff is a ritual.

What changed in the last eight hours. What is still risky. What we are waiting on. Who was paged, and whether it was real. Where the dashboard is. What the current traffic split is. What would make us halt.

We write it in the same place every time — a ticket, a doc, an incident channel, whatever your culture uses — so the next region does not depend on someone answering a ping.

During a multi-day cutover this is not optional. Phases will cross midnight. If India finds a problem at their 11 a.m., the US team should inherit a decision, not a mystery.

There is a fairness point I will not skip in a WIE room. Follow-the-sun can accidentally mean **the same region always gets the ugly hours** because that is “when the change window is.” Rotate the hard windows. Do not let geography become a caste system for toil.

The prize, when this works, is huge: 24-hour progress without 24-hour suffering for one person.

**Transition:** “When something does go wrong — and something will — the postmortem is either how you get better, or how you teach people to hide.”

---

## Slide 19 — Blameless postmortems, and trust with developers

**On the slide:** two halves if needed, or one slide with two columns: postmortem / trust.

**Time:** 3 minutes.

**Say this:**

A blameless postmortem does not mean nothing was wrong. It means we look for **conditions**, not villains.

Humans will always be near the keyboard. If your conclusion is “they should have been more careful,” you will get the same incident again with a different name on the ticket.

Better questions: What made the wrong action easy? What signal was missing? Why did the test not catch it? Why did the page not fire? Why did rollback feel scary? Which incentive pushed a date over a gate?

Write it down. Share it. Assign fixes that change the system. Then actually do those fixes. A postmortem with no follow-through is theater.

This is also how you build **trust with development teams.**

SRE can accidentally become the police: we stop releases, we own the pager, we show up with graphs. Developers will hide risk from the police. They will partner with a group that helps them ship safely.

Trust looks like this in practice.

We define SLOs together, not as a surprise. We sit in the same cutover reviews. We celebrate a no-go that protected customers. We do not use error budgets as a punishment. We use them as a shared fuel gauge: when the budget is healthy, we can change faster; when it is not, we repair first.

If you are an SRE, your best compliment from a developer is not “they are strict.” It is “they make it easier to do the right thing.”

If you are a developer in this audience, invite your reliability partners in before the week of production. Late involvement is how adversarial relationships start.

**A WIE leadership line:** “Psychological safety is not softness. It is how you get the truth while there is still time to act.”

**Transition:** “Let me put the whole talk into a roadmap you can use on Monday.”

---

## Slide 20 — A practical roadmap

**On the slide:** a numbered list, 7–9 steps, from now to after cutover. This is the slide people photograph.

**Time:** 2.5 minutes. Walk the list. Do not recap every previous story.

**Say this:**

If I were sitting with your team next week, this is the order I would use.

**1. Name the customer journeys that must not break.** If you cannot name them, you are not migrating a product. You are migrating servers.

**2. Write SLOs and the error budget in one page.** Share it with engineering and with the business partner who cares about the date.

**3. Instrument both old and new until they tell the same story.** Baseline a normal week.

**4. Design rollback, then test it.** Include the data implications.

**5. Run in parallel.** Shadow or dual-serve until mismatches are boring.

**6. Move data with independent verification and a plan for the tail.**

**7. Phase the traffic.**  Tiny, then small, then large. Gates, not dates. A named person who can halt.

**8. Staff the human system.** Follow-the-sun handoffs, extra coverage on phase days, quiet pages, a blameless review after.

**9. After 100 percent, keep watching.** Slow failures deserve a calendar, not optimism.

That is the whole talk, in one checklist. Cloud provider names are not on this list on purpose. They are implementation. This is the mindset.

**Transition:** “Three sentences I want you to remember when the slides are gone.”

---

## Slide 21 — Takeaways

**On the slide:** three short lines. Large type. No paragraphs.

**Time:** 75 seconds.

**Say this:**

One: **Zero downtime is a decision system.** Phased traffic, real rollback, parallel proof, and honest data movement. Not a maintenance window with better branding.

Two: **SLOs and error budgets are how adults argue about risk.** Use them before, during, and after cutover so go / no-go is evidence, not volume.

Three: **People are in the critical path.** Protect on-call, hand off the sun, learn in the open, and be a partner to the teams who write the code. A reliable platform with an exhausted team is a temporary platform.

If you are a woman in this field, or anyone who has been told to be grateful for a seat in the war room: you do not have to earn belonging through heroics. You can lead by making heroics unnecessary.

**Pause. Let that land. Do not fill the silence.**

**Transition:** “I will stop there so we have time for you.”

---

## Slide 22 — Thank you

**On the slide:** Thank you. Questions. Your name. Optional: employer on this slide only, plus a contact that you are willing to share. Optional: “ideas, not a product pitch.”

**Time:** 20–30 seconds, then you are in Q&A.

**Say this:**

Thank you to IEEE Women in Engineering, to the organizers, and to everyone who spent this hour with me.

I hope you take one practice — one gate, one SLO, one kinder handoff — and use it on a system that matters to you.

I would love your questions. If you are a student, you are welcome to ask the basic ones. Those are often the best.

**Then stop talking.** Smile at the camera. Let the host run the queue.

**Do not:** list ten certifications, recap the talk, or start a new topic.

---

## Slide 23 — Questions (hold this slide)

**Time:** 15 minutes.

**How to handle the room:**

- Repeat the question in one sentence so the recording and the chat both hear it.
- Answer in 60–90 seconds. Then “I can go deeper if you want.”
- If you do not know: “I have not lived that exact case. Here is how I would start to reason about it.” That sounds stronger than a fake expert answer.
- If a question pulls you toward payments, vendors, or internal numbers: “I am going to keep this at the pattern level, which travels better across industries.” Then answer the pattern.

### Questions you should be ready for

**Q: Is zero downtime realistic, or is it marketing?**  
A: Full never-fail is not realistic. Designed change, tiny blast radius, and fast reverse *are* realistic. I use “zero-downtime mindset” to mean we refuse to make the customer our test environment.

**Q: How do you pick 99.9 vs 99.99?**  
A: Start from the user journey and the cost of being down, not from a number that sounds executive. Tighter nines are expensive. They need redundancy, testing, and operational maturity. A dishonest 99.99 is worse than an honest 99.9 that you actually run to.

**Q: What if leadership refuses a no-go?**  
A: Bring the SLO and the remaining error budget, in one chart, with customer language. Ask what we will say if this fails at 100 percent. You may still lose the argument sometimes. Document the risk. Protect the team from blame you warned about. That is leadership too.

**Q: How long should dual-running last?**  
A: Long enough to see a full business cycle — a peak, a batch window, a Monday — and until mismatches are rare and understood. Not forever. Put a review date on the calendar when you start.

**Q: We are a small team. We cannot do follow-the-sun.**  
A: Then reduce pages, reduce toil, and make rollback simple. Follow-the-sun is a way to buy coverage. A small team’s version is: fewer emergencies, better runbooks, no heroics as culture.

**Q: How do I start SRE as a student?**  
A: Learn how a request travels. Learn to read a dashboard. Contribute to monitoring, tests, and incident write-ups. Reliability is systems thinking plus empathy for the user. You do not need permission to practice that on a class project.

**Q: Kubernetes / AWS / OpenShift — which should we choose?**  
A: I will not pick a vendor in this room. Choose the platform your organization can operate at 2 a.m. The constraint is operational skill, not the logo.

**Q: How do you keep women and underrepresented engineers from holding the worst on-call?**  
A: Measure who gets the pages, who gets the weekend windows, who gets the visible cutover roles. Rotate deliberately. Sponsor people into the high-judgment seats, not only into the thankless ones. If the load is unfair, that is a design bug.

**Q: What is the first thing you would fix in a messy on-call?**  
A: Delete or downgrade noisy alerts until a page means “a user is hurting.” Then write the first-five-minutes runbook for the remaining pages. Quiet plus actionable beats a beautiful platform that still wakes you for trivia.

**Q: How is this different from DevOps?**  
A: DevOps is a culture of building and running together. SRE is a specific implementation with SLOs, error budgets, and engineering work aimed at reliability. I do not fight the label. I fight unmeasured hope.

---

## If you get nervous

Your job tomorrow is not to be perfect. Your job is to be clear, kind, and concrete.

Open with gratitude. Teach with examples. Close with people. Stop on time.

You already know this material. You have lived it. IEEE WIE invited you because that combination is rare: production judgment plus a willingness to teach.

You have enough time. Practice the first 20 seconds and the last 60 seconds. The middle is you talking to engineers about work you do every week.

I will be in the room with you in this sense: if you forget a number, tell the story. If you forget a story, walk the checklist on Slide 20. You cannot get truly lost.

Good luck. You are ready to make an impression by being the most useful person on the call, not the most technical.
