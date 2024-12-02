 Day 2 - Advent of Code 2024    window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});

[Advent of Code](/)
===================

*   [\[About\]](/2024/about)
*   [\[Events\]](/2024/events)
*   [\[Shop\]](https://cottonbureau.com/people/advent-of-code)
*   [\[Settings\]](/2024/settings)
*   [\[Log Out\]](/2024/auth/logout)

   int y=[2024](/2024);
=======================

*   [\[Calendar\]](/2024)
*   [\[AoC++\]](/2024/support)
*   [\[Sponsors\]](/2024/sponsors)
*   [\[Leaderboard\]](/2024/leaderboard)
*   [\[Stats\]](/2024/stats)

Our [sponsors](/2024/sponsors) help make Advent of Code possible:

[Sony Interactive Entertainment](/2024/sponsors/redirect?url=https%3A%2F%2Fwww%2Eplaystation%2Ecom%2Fen%2Dus%2Fcorporate%2Fplaystation%2Dcareers%2F) - Pushing the boundaries of Play! A O X #

\--- Day 2: Red-Nosed Reports ---
---------------------------------

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the [Red-Nosed Reindeer nuclear fusion/fission plant](/2015/day/19) appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they _still_ talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many _reports_, one report per line. Each report is a list of numbers called _levels_ that are separated by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are _safe_. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

*   The levels are either _all increasing_ or _all decreasing_.
*   Any two adjacent levels differ by _at least one_ and _at most three_.

In the example above, the reports can be found safe or unsafe by checking those rules:

*   `7 6 4 2 1`: _Safe_ because the levels are all decreasing by 1 or 2.
*   `1 2 7 8 9`: _Unsafe_ because `2 7` is an increase of 5.
*   `9 7 6 2 1`: _Unsafe_ because `6 2` is a decrease of 4.
*   `1 3 2 4 5`: _Unsafe_ because `1 3` is increasing but `3 2` is decreasing.
*   `8 6 4 4 1`: _Unsafe_ because `4 4` is neither an increase or a decrease.
*   `1 3 6 7 9`: _Safe_ because the levels are all increasing by 1, 2, or 3.

So, in this example, `_2_` reports are _safe_.

Analyze the unusual data from the engineers. _How many reports are safe?_

Your puzzle answer was `516`.

\--- Part Two ---
-----------------

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems _tolerate a single bad level_ in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

*   `7 6 4 2 1`: _Safe_ without removing any level.
*   `1 2 7 8 9`: _Unsafe_ regardless of which level is removed.
*   `9 7 6 2 1`: _Unsafe_ regardless of which level is removed.
*   `1 _3_ 2 4 5`: _Safe_ by removing the second level, `3`.
*   `8 6 _4_ 4 1`: _Safe_ by removing the third level, `4`.
*   `1 3 6 7 9`: _Safe_ without removing any level.

Thanks to the Problem Dampener, `_4_` reports are actually _safe_!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. _How many reports are now safe?_

Your puzzle answer was `561`.

Both parts of this puzzle are complete! They provide two gold stars: \*\*

At this point, you should [return to your Advent calendar](/2024) and try another puzzle.

If you still want to see it, you can [get your puzzle input](2/input).

You can also \[Shareon [Bluesky](https://bsky.app/intent/compose?text=I%27ve+completed+%22Red%2DNosed+Reports%22+%2D+Day+2+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F2) [Twitter](https://twitter.com/intent/tweet?text=I%27ve+completed+%22Red%2DNosed+Reports%22+%2D+Day+2+%2D+Advent+of+Code+2024&url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F2&related=ericwastl&hashtags=AdventOfCode) [Mastodon](javascript:void(0);)\] this puzzle.

(function(i,s,o,g,r,a,m){i\['GoogleAnalyticsObject'\]=r;i\[r\]=i\[r\]||function(){ (i\[r\].q=i\[r\].q||\[\]).push(arguments)},i\[r\].l=1\*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)\[0\];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','//www.google-analytics.com/analytics.js','ga'); ga('create', 'UA-69522494-1', 'auto'); ga('set', 'anonymizeIp', true); ga('send', 'pageview');
