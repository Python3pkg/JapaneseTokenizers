#! -*- coding: utf-8 -*-
import sys
import os
from JapaneseTokenizer import JumanWrapper
from JapaneseTokenizer import MecabWrapper
from JapaneseTokenizer import TokenizedSenetence
from JapaneseTokenizer import FilteredObject
from JapaneseTokenizer import KyteaWrapper
from JapaneseTokenizer.datamodels import TokenizedResult
__author__ = 'kensuke-mi'

python_version = sys.version_info

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for python2.x

def basic_example_mecab_2x():
    # ========================================================
    # TOKENIZE
    # ========================================================

    # input is `unicode` type(in python2x)
    sentence = u'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'

    # make MecabWrapper object
    # path where `mecab-config` command exists. You can check it with `which mecab-config`
    # default value is '/usr/local/bin'
    path_mecab_config='/usr/local/bin'

    # you can choose from "neologd", "all", "ipaddic", "user", ""
    # "ipadic" and "" is equivalent
    dictType = "neologd"

    mecab_wrapper = MecabWrapper(dictType=dictType, path_mecab_config=path_mecab_config)

    # tokenize sentence. Returned object is list of tuples
    tokenized_obj = mecab_wrapper.tokenize(sentence=sentence)
    assert isinstance(tokenized_obj, list)

    # Returned object is "TokenizedSenetence" class if you put return_list=False
    tokenized_obj = mecab_wrapper.tokenize(sentence=sentence, return_list=False)
    assert isinstance(tokenized_obj, TokenizedSenetence)

    # ========================================================
    # FILTERING
    # ========================================================
    # you can filter tokens by stopwords or POS conditions

    # stopword is list objetc
    stopwords = [u'テヘラン']
    assert isinstance(tokenized_obj, TokenizedSenetence)
    # returned object is "FilteredObject" class
    filtered_obj = mecab_wrapper.filter(
        parsed_sentence=tokenized_obj,
        stopwords=stopwords
    )
    assert isinstance(filtered_obj, FilteredObject)
    #
    print('-'*30)
    print(u'Mecab Demo')
    for token_obj in filtered_obj.tokenized_objects:
        assert isinstance(token_obj, TokenizedResult)
        print(u'word_stem:{}, word_surafce:{}, pos:{}'.format(
            token_obj.word_stem,
            token_obj.word_surface,
            token_obj.tuple_pos))

    # pos condition is list of tuples
    # You can set POS condition "ChaSen 品詞体系 (IPA品詞体系)" of this page http://www.unixuser.org/~euske/doc/postag/#chasen
    pos_condition = [(u'名詞', u'固有名詞'), (u'動詞', u'自立')]
    filtered_obj = mecab_wrapper.filter(
        parsed_sentence=tokenized_obj,
        pos_condition=pos_condition
    )
    assert isinstance(filtered_obj, FilteredObject)
    print('-'*30)
    print(u'Mecab Filtering Demo')
    for token_obj in filtered_obj.tokenized_objects:
        assert isinstance(token_obj, TokenizedResult)
        print(u'word_stem:{}, word_surafce:{}, pos:{}'.format(
            token_obj.word_stem,
            token_obj.word_surface,
            token_obj.tuple_pos))


def basic_example_juman_2x():
    # input is `unicode` type(in python2x)
    sentence = u'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'

    juman_wrapper = JumanWrapper()
    tokenized_objects = juman_wrapper.tokenize(
        sentence=sentence,
        normalize=True,
        return_list=False
    )
    assert isinstance(tokenized_objects, TokenizedSenetence)
    print('-'*30)
    print(u'Juman Demo')
    for token_object in tokenized_objects.tokenized_objects:
        assert isinstance(token_object, TokenizedResult)
        print(u'word_stem:{}, word_surafce:{}, pos:{}'.format(
            token_object.word_stem,
            token_object.word_surface,
            token_object.tuple_pos))

    # filtering is same as mecab


def basic_example_kytea_2x():
    # input is `unicode` type(in python2x)
    sentence = u'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'

    kytea_wrapper = KyteaWrapper()
    tokenized_objects = kytea_wrapper.tokenize(
        sentence=sentence,
        normalize=True,
        return_list=False
    )
    assert isinstance(tokenized_objects, TokenizedSenetence)
    print('-'*30)
    print(u'Kytea Demo')
    for token_object in tokenized_objects.tokenized_objects:
        assert isinstance(token_object, TokenizedResult)
        # kytea does not show word stem, thus word_stem attribute is always null string
        # instead kytea tells you inferred Yomi, pronounciation
        print(u'word_surafce:{}, pos:{}, yomi:{}, yomi_score:{}'.format(
            token_object.word_surface,
            token_object.tuple_pos,
            token_object.misc_info['yomi'],
            token_object.misc_info['yomi_score'],
        ))

def advanced_example_mecab_2x():
    # ========================================================
    # USE YOUE OWN DICTIONARY
    # with your own dictionary, you can force Mecab to make some word into one token
    # ========================================================
    # make your own "user dictionary" with CSV file
    # To know more about this file, see this page(sorry, Japanese only) https://mecab.googlecode.com/svn/trunk/mecab/doc/dic.html
    example_user_dict = "userdict.csv"

    # set dictType='user' or dictType='all'
    # set pathUserDictCsv
    mecab_wrapper = MecabWrapper(
        dictType='user',
        pathUserDictCsv=example_user_dict
    )
    print('-'*30)
    print(u'Mecab UserDictionary Demo')
    sentence = u'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'
    tokenized_obj = mecab_wrapper.tokenize(sentence, return_list=False)
    assert isinstance(tokenized_obj, TokenizedSenetence)
    for token_obj in tokenized_obj.tokenized_objects:
        assert isinstance(token_obj, TokenizedResult)
        if token_obj.word_stem == u'ペルシア語':
            print(token_obj.word_stem)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for python3.x

def basic_example_3x():
    # ========================================================
    # TOKENIZE
    # ========================================================

    # In python3x, you don't mind it
    sentence = 'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'

    # make MecabWrapper object
    # path where `mecab-config` command exists. You can check it with `which mecab-config`
    # default value is '/usr/local/bin'
    path_mecab_config='/usr/local/bin'

    # you can choose from "neologd", "all", "ipaddic", "user", ""
    # "ipadic" and "" is equivalent
    dictType = ""

    mecab_wrapper = MecabWrapper(dictType=dictType)

    # tokenize sentence. Returned object is list of tuples
    tokenized_obj = mecab_wrapper.tokenize(sentence=sentence)
    assert isinstance(tokenized_obj, list)

    # Returned object is "TokenizedSenetence" class if you put return_list=False
    tokenized_obj = mecab_wrapper.tokenize(sentence=sentence, return_list=False)
    assert isinstance(tokenized_obj, TokenizedSenetence)

    # ========================================================
    # FILTERING
    # ========================================================
    # you can filter tokens by stopwords or POS conditions

    # stopword is list objetc
    stopwords = ['テヘラン']
    assert isinstance(tokenized_obj, TokenizedSenetence)
    # returned object is "FilteredObject" class
    filtered_obj = mecab_wrapper.filter(
        parsed_sentence=tokenized_obj,
        stopwords=stopwords
    )
    assert isinstance(filtered_obj, FilteredObject)

    # pos condition is list of tuples
    # You can set POS condition "ChaSen 品詞体系 (IPA品詞体系)" of this page http://www.unixuser.org/~euske/doc/postag/#chasen
    pos_condition = [('名詞', '固有名詞'), ('動詞', '自立')]
    filtered_obj = mecab_wrapper.filter(
        parsed_sentence=tokenized_obj,
        pos_condition=pos_condition
    )
    assert isinstance(filtered_obj, FilteredObject)


def advanced_example_3x():
    # ========================================================
    # USE YOUE OWN DICTIONARY
    # with your own dictionary, you can force Mecab to make some word into one token
    # ========================================================
    # make your own "user dictionary" with CSV file
    # To know more about this file, see this page(sorry, Japanese only) https://mecab.googlecode.com/svn/trunk/mecab/doc/dic.html
    example_user_dict = "userdict.csv"

    # set dictType='user' or dictType='all'
    # set pathUserDictCsv
    mecab_wrapper = MecabWrapper(
        dictType='user',
        pathUserDictCsv=example_user_dict
    )
    sentence = 'テヘラン（ペルシア語: تهران  ; Tehrān Tehran.ogg 発音[ヘルプ/ファイル]/teɦˈrɔːn/、英語:Tehran）は、西アジア、イランの首都でありかつテヘラン州の州都。人口12,223,598人。都市圏人口は13,413,348人に達する。'
    tokenized_obj = mecab_wrapper.tokenize(sentence, return_list=False)
    assert isinstance(tokenized_obj, TokenizedSenetence)
    for token_obj in tokenized_obj.tokenized_objects:
        assert isinstance(token_obj, TokenizedResult)
        if token_obj.word_stem == 'ペルシア語':
            print(token_obj.word_stem)


if __name__ == "__main__":
    if python_version >= (3, 0, 0):
        basic_example_3x()
        advanced_example_3x()
    else:
        basic_example_mecab_2x()
        advanced_example_mecab_2x()
        basic_example_juman_2x()
        basic_example_kytea_2x()