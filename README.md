# € language

A language created for [code golf][Code golf].

A page about this language has been created on [esolangs][esolang].

Builds: 
[![Build status][Travis Master image]][Travis Master]

## Explanation

I spend most of my time on PHP scripts and it brought me a question: why am I forced to use `$` for my variables names?
€ is my local currency, so let's use it! Since € is used in many countries, I used some words from EU languages as keywords.

Keywords:

- `gleich` is equal in German
- `mientras` is while in Spanish
- `topo` is greater in Portuguese (update: it should be maior instead, thanks to [acrolith][acrolith] for the tip)
- `odejmowanie` is subtract in Polish
- `afficher` is print in French
- newlines are called `nl` sometimes, and the TLD of `NETHERLANDS` is `nl`, so I defined a constant `NETHERLANDS` to display newlines

I cheated a little bit since there is no `if` keyword, I chose to directly print the last two lines.

### Example

[./euro.eu](./euro.eu)

### Interpreter in Python

[./euro.py](./euro.py)

The interpreter won't do more than execute the script to display 99 bottles of beers.

To run it, save both files then run the Python file with the `.eu` script as an argument:

```shell
$ python euro.py euro.eu
```

[Code golf]: https://codegolf.stackexchange.com/a/25240/10619

[esolang]: https://esolangs.org/wiki/%E2%82%AC

[Travis Master image]: https://travis-ci.com/alexislefebvre/euro-language.svg?branch=master
[Travis Master]: https://travis-ci.com/alexislefebvre/euro-language

[acrolith]: https://codegolf.stackexchange.com/users/56258/acrolith

To run it, save both files then run the Python file with the .eu script as an argument:
