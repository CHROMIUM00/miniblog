DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS comment;

CREATE TABLE user
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT        NOT NULL
);

CREATE TABLE post
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    author      TEXT      NOT NULL,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title       TEXT      NOT NULL,
    body        TEXT      NOT NULL,
    description TEXT      NOT NULL
);

CREATE TABLE comment
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER   NOT NULL,
    author  TEXT      NOT NULL,
    mail    TEXT      NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT      NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post (id)
)


INSERT INTO comment (id, post_id, author, mail, created, content) VALUES (1, 3, 'averagecommentlover', '123@abc.com', '2024-12-09 14:39:38', 'the quick brown fox jumps over the lazy dog');
INSERT INTO comment (id, post_id, author, mail, created, content) VALUES (2, 3, 'Anonymous', 'anonymous@anonymous.com', '2024-12-09 15:46:41', 'nihao');

INSERT INTO post (id, author, created, title, body, description) VALUES (1, 'me', '2024-12-07 14:03:32', 'test#1', 'omggggggggggggg', 'nihao');
INSERT INTO post (id, author, created, title, body, description) VALUES (2, 'alsome', '2024-12-08 10:21:01', 'hgreigntsh', '<p><em>nihao</em>ginguiresngiurneaig</p>\n', 'tett');
INSERT INTO post (id, author, created, title, body, description) VALUES (3, 'mdit', '2024-12-08 12:08:21', 'mdtest', '<h1>h1 Heading</h1>
<h2>h2 Heading</h2>
<h3>h3 Heading</h3>
<h4>h4 Heading</h4>
<h5>h5 Heading</h5>
<h6>h6 Heading</h6>
<h2>Horizontal Rules</h2>
<hr>
<hr>
<hr>
<h2>Typographic replacements</h2>
<p>Enable typographer option to see result.</p>
<p>© © ® ® ™ ™ (p) (P) ±</p>
<p>test… test… test… test?.. test!..</p>
<p>!!! ??? ,  – —</p>
<p>“Smartypants, double quotes” and ‘single quotes’</p>
<h2>Emphasis</h2>
<p><strong>This is bold text</strong></p>
<p><strong>This is bold text</strong></p>
<p><em>This is italic text</em></p>
<p><em>This is italic text</em></p>
<p><s>Strikethrough</s></p>
<h2>Blockquotes</h2>
<blockquote>
<p>Blockquotes can also be nested…</p>
<blockquote>
<p>…by using additional greater-than signs right next to each other…</p>
<blockquote>
<p>…or with spaces between arrows.</p>
</blockquote>
</blockquote>
</blockquote>
<h2>Lists</h2>
<p>Unordered</p>
<ul>
<li>Create a list by starting a line with <code>+</code>, <code>-</code>, or <code>*</code></li>
<li>Sub-lists are made by indenting 2 spaces:
<ul>
<li>Marker character change forces new list start:
<ul>
<li>Ac tristique libero volutpat at</li>
</ul>
<ul>
<li>Facilisis in pretium nisl aliquet</li>
</ul>
<ul>
<li>Nulla volutpat aliquam velit</li>
</ul>
</li>
</ul>
</li>
<li>Very easy!</li>
</ul>
<p>Ordered</p>
<ol>
<li>
<p>Lorem ipsum dolor sit amet</p>
</li>
<li>
<p>Consectetur adipiscing elit</p>
</li>
<li>
<p>Integer molestie lorem at massa</p>
</li>
<li>
<p>You can use sequential numbers…</p>
</li>
<li>
<p>…or keep all the numbers as <code>1.</code></p>
</li>
</ol>
<p>Start numbering with offset:</p>
<ol start="57">
<li>foo</li>
<li>bar</li>
</ol>
<h2>Code</h2>
<p>Inline <code>code</code></p>
<p>Indented code</p>
<pre><code>// Some comments
line 1 of code
line 2 of code
line 3 of code
</code></pre>
<p>Block code “fences”</p>
<pre><code class="hljs">Sample text here...
</code></pre>
<p>Syntax highlighting</p>
<pre class="hljs language-js"><code><span class="hljs-keyword">var</span> foo = <span class="hljs-keyword">function</span> (<span class="hljs-params">bar</span>) {
  <span class="hljs-keyword">return</span> bar++;
};

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title function_">foo</span>(<span class="hljs-number">5</span>));
</code></pre>
<h2>Tables</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td>path to data files to supply the data that will be passed into templates.</td>
</tr>
<tr>
<td>engine</td>
<td>engine to be used for processing templates. Handlebars is the default.</td>
</tr>
<tr>
<td>ext</td>
<td>extension to be used for dest files.</td>
</tr>
</tbody>
</table>
<p>Right aligned columns</p>
<table>
<thead>
<tr>
<th style="text-align:right">Option</th>
<th style="text-align:right">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right">data</td>
<td style="text-align:right">path to data files to supply the data that will be passed into templates.</td>
</tr>
<tr>
<td style="text-align:right">engine</td>
<td style="text-align:right">engine to be used for processing templates. Handlebars is the default.</td>
</tr>
<tr>
<td style="text-align:right">ext</td>
<td style="text-align:right">extension to be used for dest files.</td>
</tr>
</tbody>
</table>
<h2>Links</h2>
<p><a href="http://dev.nodeca.com">link text</a></p>
<p><a href="http://nodeca.github.io/pica/demo/" title="title text!">link with title</a></p>
<p>Autoconverted link <a href="https://github.com/nodeca/pica">https://github.com/nodeca/pica</a> (enable linkify to see)</p>
<h2>Images</h2>
<p><img src="https://octodex.github.com/images/minion.png" alt="Minion">
<img src="https://octodex.github.com/images/stormtroopocat.jpg" alt="Stormtroopocat" title="The Stormtroopocat"></p>
<p>Like links, Images also have a footnote style syntax</p>
<p><img src="https://octodex.github.com/images/dojocat.jpg" alt="Alt text" title="The Dojocat"></p>
<p>With a reference later in the document defining the URL location:</p>', 'testing md');

INSERT INTO user (id, username, password) VALUES (1, 'CHROMIUM00', 'scrypt:32768:8:1$UrJMQZ033hhhrcvp$18c59d2a1eb6c1b0853b9c508edbca43e31efdf8fde666cf87c7b9a80d60388c878890d1a2e6c3f1773d7c1cfb145c828bc5c932a19050c042aef3fb4da15638');
