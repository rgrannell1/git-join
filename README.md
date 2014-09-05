git join
----------------

A common git workflow involves maintaining three tiers of branch; transient feature branches, a development
version branch, and a release branch.

Feature branches are created for any new functionality you want to add to the next version of your program;
these are merged into development when they are finished, and then deleted.

The development branch holds the work-in-progress version of your program; you update it by merging in feature branches, and
occasionally committing directly to fix bugs.

The releases branch represents publically usable versions of your code. You never directly commit to this branch, but instead
you merge the development branch when your tests are green and you've finished adding features to this version.


```
                    A --- B --- C --- D       feat-Foo
                   /
o --- o --- o --- o                           development
       \
        o                                     releases
```

Git join makes merging feature branches easier; it merges the branch and then deletes it.

```
o --- o --- o --- o --- A --- B --- C --- D   development
       \
        o                                     releases
```

### Requirements.

* Git.

### Installation.

To install git join run the following

```bash
wget -q -O - https://raw.githubusercontent.com/rgrannell1/git-join/master/install.sh | bash
```

## License.

"git join" is released under the MIT licence.

The MIT License (MIT)

Copyright (c) 2014 Ryan Grannell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Versioning.

All versions post-release will be compliant with the Semantic Versioning 2.0.0 standard.

http://semver.org/
