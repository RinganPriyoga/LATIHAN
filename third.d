import std.stdio;
import std.string;
import std.ascii;
import std.regex;
import std.conv;
import std.algorithm;
import std.file;

void main(string[] args)
{
    string[] files = ["Text1.txt", "Text2.txt", "Text3.txt", "Text4.txt", "Text5.txt", "Text6.txt"];
    string[] conj = [
         "after", "albeit", "although", "and", "as", "because", "before", "but",
         "for", "if", "nor", "or", "since", "so", "than", "that", "though", "till",
         "unless", "until", "when", "where", "whereas", "whether", "while", "with",
         "yet", "though", "lest", "once", "whenever", "wherever", "whilst", "otherwise",
         "inasmuch", "inasmuch as", "providing", "provided", "scarcely", "whereupon",
         "hereupon", "notwithstanding", "now", "because", "although", "even",
         "either", "neither", "even though", "whether or not", "rather", "nor",
         "both", "but only", "not only", "though that", "so that", "till now",
         "unless that", "while now", "on", "hence", "thus", "therefore",
         "consequently", "meanwhile", "moreover", "furthermore", "besides",
         "afterwards", "thereupon", "accordingly", "yet when", "once before",
         "even so", "since when", "henceforth", "even then", "so long as",
         "given", "granted", "forasmuch", "inasfar", "seeing", "seeing that",
         "even if", "just as", "as though", "even when", "notwithstanding",
         "only if", "beforehand", "as of now"
    ];

    int totalWords;
    alias wordInArticle = int[string];
    wordInArticle totalWordOccurrences;
    wordInArticle totalAlphaNum;
    wordInArticle totalConjunctions;

    foreach (string path; files)
    {
        int articleWords = 0;
        wordInArticle wordCount;
        wordInArticle alphaNum;
        wordInArticle conjunctions;
        string textData = readText(path);
        auto re = regex(r"\[\d+\]");
        auto reNonAlpha = regex(r"[^a-zA-Z\d\s:]");
        string filtered;
        filtered = replaceAll(textData, re, "");
        filtered = replaceAll(filtered, reNonAlpha, "");
        string[] splitTextData = filtered.split();

        writeln(path, " has ", splitTextData.length, " words.");

        totalWords += splitTextData.length;
        articleWords = to!int(splitTextData.length);

        foreach (string word; splitTextData)
        {
            wordCount[word] += 1;
            totalWordOccurrences[word] += 1;
            if (conj.canFind(word))
            {
                conjunctions[word] += 1;
                totalConjunctions[word] += 1;
                continue;
            }
            foreach (dchar ch; word)
            {
                alphaNum[ch.to!string] += 1;
                totalAlphaNum[ch.to!string] += 1;
            }
        }

        writeln("=======================================");
        writeln("Article: ", path);
        writeln("Word occurrences:");
        foreach (string word, int count; wordCount)
        {
            writeln(word, ": ", count);
        }

        writeln("\nDetected conjunctions:");
        foreach (string word, int count; conjunctions)
        {
            writeln(word, ": ", count);
        }

        writeln("\nAlphanumeric occurrences:");
        foreach (string ch, int count; alphaNum)
        {
            writeln(ch, ": ", count);
        }
        writeln("=======================================");
    }

    writeln("\nTotal word occurrences:");
    foreach (string word, int count; totalWordOccurrences)
    {
        writeln(word, ": ", count);
    }

    writeln("\nTotal words: ", totalWords);

    writeln("\nTotal detected conjunctions:");
    foreach (string word, int count; totalConjunctions)
    {
        writeln(word, ": ", count);
    }

    writeln("\nTotal alphanumeric occurrences:");
    foreach (string ch, int count; totalAlphaNum)
    {
        writeln(ch, ": ", count);
    }
}

