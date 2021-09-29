# __Multiple Sentence Reconstruction__

- input data

```tex:input.txt
hello world. it's a song that we're singing.
```

__↓__ 3 type conversion

- paragraph formating

```tex
hello world.
it's a song that we're singing.
```

- trancerated

```tex
こんにちは世界。
歌っている歌です。
```

- trancerated before and after

```tex
hello world.
こんにちは世界。
it's a song that we're singing.
歌っている歌です。
```

---

## __Overview__

論文など翻訳したい文章をピリオド区切りで改行、翻訳します。

DeepLのアカウントを作成し、個別のauth_keyを持っていればDeepLによる翻訳も可能です。

---

## __Requirement__

```tex
Python 3.9.4
```

---

## __Installation__

Download this folder.

```shell
svn export https://github.com/06keito/sharing_function/tree/main/Multiple_sentence_reconstruction
```

---

## __Usage__

1.DeepLのauth_keyを所持しているならば、`deepl_auth_key.txt` に書き込みます。

- [DeepL API](https://www.deepl.com/docs-api)

2.googletransとdeeplライブラリをインストールします。

```shell
pip install googletrans==4.0.0-rc1 deepl
```

3.引数を指定して実行を行います。

```shell
python Multiple_sentence_reconstruction.py --mode [google_trance,deepl]
```

---

## __Author__

- [Twitter](https://twitter.com/yamamoooooooon_)

- [GiuHub](https://github.com/06keito)

---

## __Licence__

- [MIT](https://opensource.org/licenses/mit-license.php)