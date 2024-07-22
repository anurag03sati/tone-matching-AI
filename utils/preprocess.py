import re
import json

class TextCleaner:
    def __init__(self):
        self.filler_words = {
            'um', 'uh', 'like', 'you know', 'i mean', 'basically', 'actually', 'sure', 'yeah', 'and', 'so', 'if', 'we',
            'those','Wait.','No.','umm','Umm','thanks.','meet','right.','Wow,','yes, ','umm.','ok.','ok,','thank','umm, '
            'crazy', 'very', 'just', 'about', 'thanks', 'ok', 'right', 'excuse', 'me', 'well', 'sort', 'of', 'kind',
            'anyway','you.','yeah,','OK.','Uh.',"I'll",'anything','Amazing.','was','focus','focused','umm,',
            'alright', 'ah', 'oh', 'really', 'see', 'literally', 'totally', 'seriously', 'exactly', 'honestly',
            'believe', 'trust','best','perfect.','favorite','question.','own','can','sure.',
            'at', 'the', 'end', 'day', 'to', 'be', 'frank', 'let', 'think', 'in', 'fact', 'as', 'a', 'matter', 'what',
            'is', 'get','awesome.','mean.','brilliantly','Mm-hmm.','you,','um,','right.','ohh.','umm. ','umm.',
            'it', 'example', 'feel', 'think', 'that', 'guess', 'suppose', 'reckon', 'other', 'words', 'mean', 'say',
            'my', 'opinion','super.','probably','totally.','OK.',
            'personally', 'may', 'ask', 'way', 'I’m', 'concerned', 'tell', 'not', 'for', 'instance', 'is', 'sense',
            'something','funny.','cool.','Ohh.',
            'fair', 'enough', 'could', 'sort', 'like', 'to', 'put', 'point', 'indeed', 'do', 'know', 'what', 'you',
            'saying', 'Im',
            'perspective', 'as', 'far', 'from', 'if', 'impressions', 'yeah', 'very', 'good', 'a', 'to', 'in', 'It', 'be',
            'an', 'are', 'in', 'uh', 'um', 'ah', 'oh', 'hmm', 'well', 'okay', 'OK', 'yeah', 'yes', 'no', 'but', 'or',
            'because','hmm.'
            'also', 'actually', 'basically', 'seriously', 'literally', 'totally', 'really', 'just', 'right', 'exactly',
            'you know',
            'I mean', 'kind of', 'sort of', 'anyway', 'alright', 'so', 'then', 'and then', 'like', 'you see', 'listen',
            'here',
            'there', 'well', 'um', 'right', 'sure', 'alright', 'basically', 'really', 'so', 'yeah', 'no', 'but', 'or',
            'and', 'if',
            'though', 'although', 'even though', 'as well', 'still', 'just', 'even', 'well', 'you know', 'I guess',
            'I suppose',
            'I think', 'I feel', 'to be honest', 'honestly', 'frankly', 'in fact', 'indeed', 'believe me', 'trust me',
            'let me see',
            'let me think', 'like I said', 'as I said', 'I mean to say', 'what I mean is', 'the thing is',
            'the point is',
            'in other words', 'to put it simply', 'let me put it this way', 'you get what I mean',
            'do you know what I mean','always',
            'you know what Im saying', 'the way I see it', ' if you ask me', 'personally', 'from my perspective',
            ' in my opinion','amazing.','amazing,','mm-hmm.',
            'as far as I’m concerned', 'to tell you the truth', 'believe it or not', 'for example', 'for instance',
            'that is to say','yeah.','crazy.','wow,',"that's",'that.','thank','great.',
            'in a way', 'in a sense', 'you know what', 'you know something', 'to be fair', 'fair enough', 'I reckon',
            'I guess you could say',
            'I suppose you could say', 'sort of like', 'kind of like', 'yeah', 'sure', 'okay', 'great', 'cool',
            'awesome', 'nice', 'interesting',
            'fantastic', 'wonderful', 'amazing', 'brilliant', 'perfect', 'incredible', 'super', 'terrific', 'fabulous',
            'phenomenal','Amazing.',
            'outstanding', 'exceptional', 'remarkable', 'extraordinary', 'marvelous', 'excellent', 'splendid', 'lovely',
            'delightful',"it'll",
            'charming', 'gorgeous', 'beautiful', 'loved it', 'enjoyed it', 'fascinating', 'captivating', 'enthralling',
            'engaging','yeah.'
            'stimulating', 'absorbing', 'compelling', 'intriguing', 'thought-provoking', 'thoughtful', 'provocative',
            'insightful','Umm. ','Umm','that,','uh.','a?','so,',"i'm.",'hmm,',
            'started', 'through', 'working', 'before', 'after', 'then', 'there', 'been', 'had', 'like', 'with', 'when',
            'about','where,','of.',
            'since', 'back', 'also', 'where', 'more', 'most', 'even', 'some', 'many', 'other', 'both', 'into', 'over',
            'years',
            'how', 'so', 'yeah', 'right', 'um', 'well', 'cool', 'great', 'OK', 'anyways', 'wow', 'ohh', 'nice', 'hmm',
            'funny',
            'you', 'I', 'me', 'us', 'them', 'their', 'our', 'my', 'your', 'he', 'she', 'it', 'they', 'we', 'that',
            'those', 'this','out',"i'd",'able','did','did.',"i'm",'would','lot','bit','care','yes,','yes, ',
            'these', 'which', 'what', 'who', 'why', 'where', 'when', 'but', 'or', 'and', 'if', 'though', 'although',
            'because',
            'even though', 'as well', 'still', 'just', 'actually', 'really', 'seriously', 'literally', 'totally',
            'basically',
            'simply', 'exactly', 'to be honest', 'honestly', 'frankly', 'in fact', 'indeed', 'trust me', 'believe me',
            'you know','i',
            'let me see', 'let me think', 'you see', 'do you know what I mean', 'you know what I mean', 'the thing is',
            'the point is','so.', 'take care','wait.',"it's","i've",
            'in other words', 'to put it simply', 'let me put it this way', 'the way I see it', 'if you ask me',
            'personally', 'from my perspective',
            'in my opinion', 'as far as I’m concerned', 'to tell you the truth', 'believe it or not', 'for example',
            'for instance',
            'that is to say', 'in a way', 'in a sense', 'fair enough', 'I reckon', 'I guess you could say',
            'sort of like', 'kind of like','wow,','ohh.','now'
        }

    def remove_timestamps(self, text):
        """Remove timestamps from the text using regex."""
        return re.sub(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+', '', text)

    def remove_filler_words(self, text):
        """Remove filler words from the text."""
        words = text.split('\n')  # Split by newline to preserve lines

        filtered_lines = []
        for line in words:
            filtered_words = [word for word in line.split() if word.lower() not in self.filler_words]
            filtered_lines.append(' '.join(filtered_words))
        return '\n'.join(filtered_lines)

    def clean_punctuation_spaces(self, text):
        """Clean extra spaces and punctuation from the text."""
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        return text.strip()  # Remove leading/trailing spaces

    def extract_lines_before_timestamps(self, text):
        lines = text.split('\n')  # Split by newline
        extracted_lines = []
        timestamp_pattern = re.compile(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+')
        for line in lines:
            if not timestamp_pattern.match(line.strip()):
                extracted_lines.append(line.strip())
        return extracted_lines

    def extract_key_value_pairs(self, text):
        """Extract key-value pairs from the lines."""
        lines = self.extract_lines_before_timestamps(text)
        result = []
        i = 0
        while i < len(lines):
            if lines[i] == '':
                i += 1
                continue
            new_dict = {}
            key = lines[i].strip()
            value = lines[i + 1].strip() if i + 1 < len(lines) else ""
            new_dict[key] = value
            result.append(new_dict)
            i += 2  # Move to the next key-value pair

        with open('output2.json', 'w') as f:
            f.write('[')
            first = True
            for item in result:
                if (list(item.values())[0] != ''):
                    if not first:
                        f.write(',')
                    json.dump(item, f)
                    first = False
                    f.write('\n')
            f.write(']')
        return result


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def transform(self, text):
        """Run the cleaning text pipeline."""
        for step in self.steps:
            text = step(text)
        return text


# Example usage function
def run_pipeline(example_text):
    cleaner = TextCleaner()

    pipeline = Pipeline(steps=[
        cleaner.remove_timestamps,
        cleaner.remove_filler_words,
        #cleaner.clean_punctuation_spaces  # Include if needed
    ])

    processed_text = pipeline.transform(example_text)
    key_value_pairs = cleaner.extract_key_value_pairs(processed_text)

    #print(key_value_pairs)
    with open('output2.json', 'r') as f:
        data = json.load(f)

    # Create a mapping of unique keys to sequential numbers
    key_mapping = {}
    current_index = 1

    for item in data:
        key = list(item.keys())[0]
        if key not in key_mapping:
            key_mapping[key] = current_index
            current_index += 1


    for item in data:
        key = list(item.keys())[0]
        mapped_number = key_mapping[key]
        item[mapped_number] = item[key]
        del item[key]

    number_to_name_mapping = []
    for name, number in key_mapping.items():
        number_to_name_mapping.append({number: name})

    final_data =  number_to_name_mapping + data

    with open('mapped_output.json', 'w') as f:
        f.write('[')
        cnt = 0
        for item in final_data:
            cnt += 1
            json.dump(item, f)
            if (cnt != len(final_data)):
                f.write(',')
            #f.write('\n')
        f.write(']')


    print("Mapping completed and saved to mapped_output.json")

# Example text
example_text = '''

Karolina | Book Designer
OK, for sure.
0:0:18.650 --> 0:0:26.100
Karolina | Book Designer
And so I I have a designer and I help outdoors there.
0:0:26.240 --> 0:0:33.610
Karolina | Book Designer
Take their stories or ground and help turn their their manuscripts into books and illustrate it.
0:0:33.820 --> 0:0:37.730
Karolina | Book Designer
Not illustrated and show it as a cover as well.
0:0:38.80 --> 0:0:45.630
Karolina | Book Designer
So I take care of both the book cover and the interior as well, and I work mostly with self publishing authors.
0:0:46.730 --> 0:0:52.290
Karolina | Book Designer
Umm, yeah, so this is this is the business itself and how I started.
0:0:53.270 --> 0:0:57.610
Karolina | Book Designer
Umm, that's actually a long story, so I have.
0:0:59.540 --> 0:1:1.230
Karolina | Book Designer
My background isn't writing.
0:1:1.330 --> 0:1:16.660
Karolina | Book Designer
I've been studying philology and literature and language and after that journalism as well, and I've been working as a journalist for a few years back in Poland, because this is where I'm from.
0:1:17.650 --> 0:1:23.100
Karolina | Book Designer
Umm and I, so I was writing and at some point I was.
0:1:23.110 --> 0:1:33.490
Karolina | Book Designer
I had also a travel blog and I started to do some graphic design for my blog because I needed that and I really like it.
0:1:33.500 --> 0:1:52.170
Karolina | Book Designer
So I at some point I was going deeper and deeper into graphic design and when I moved, when I came to Canada the first time, because this is kind of my second time I was here on one year visa earlier and I knew that I might not be coming back to Poland.
0:1:52.180 --> 0:1:57.70
Karolina | Book Designer
So I wanted to start doing on top of my nine to five job.
0:1:57.80 --> 0:2:10.810
Karolina | Book Designer
I wanted to start doing some freelance work because I've been always pronouncing back in Poland and I started to go into graphic design because I didn't feel as comfortable writing in English as I was in Polish.
0:2:10.820 --> 0:2:23.520
Karolina | Book Designer
So I just I I didn't want to stick with the writing itself and then I was just doing general, some marketing, graphic design stuff I didn't use down.
0:2:23.530 --> 0:2:25.830
Karolina | Book Designer
I didn't know what I wanna do in graphic design.
0:2:27.950 --> 0:2:41.420
Karolina | Book Designer
Until I got a gig for doing audio book covers for European publisher and after doing like two or three covers for them, I just fell in love with it and I knew that this is what I wanted to do.
0:2:42.470 --> 0:2:49.550
Karolina | Book Designer
And then I got pregnant, which added like a new layer to to all that.
0:2:49.900 --> 0:2:55.280
Karolina | Book Designer
And we came back to Canada when my son was three months old in 2019.
0:2:56.780 --> 0:2:58.570
Karolina | Book Designer
And I couldn't.
0:2:58.580 --> 0:3:1.170
Karolina | Book Designer
I didn't go back to to my regular work.
0:3:1.180 --> 0:3:14.320
Karolina | Book Designer
I stayed home with with my son and I knew I want to do the freelance work more and more and just, you know, do my own thing, not work for somebody and then pandemic hit.
0:3:15.260 --> 0:3:15.520
Emma Bergin
Yeah.
0:3:16.200 --> 0:3:31.400
Karolina | Book Designer
Yeah, another another difficulty when you're trying to meet people and grow your network is you know, while we were here for the first time with my husband, having just one year working visa and you don't and we have, we have.
0:3:31.410 --> 0:3:38.590
Karolina | Book Designer
But we have like a lot of experience with traveling and meeting people and then leaving friendship behind, which was pretty hard.
0:3:39.610 --> 0:3:44.950
Karolina | Book Designer
So when we were here and we knew that we're here only for a year, we didn't.
0:3:52.150 --> 0:3:52.350
Emma Bergin
Yeah.
0:3:45.10 --> 0:3:52.390
Karolina | Book Designer
We weren't looking for any, you know, deep friendship and meaningful relationships because we didn't want to get hurt again once we live.
0:3:53.120 --> 0:3:56.850
Karolina | Book Designer
Umm, but then we came back here and what what?
0:3:56.860 --> 0:4:9.660
Karolina | Book Designer
That that first year that we didn't build those relationships when that did is that when we came back, we were kind of coming, you know, into new place, new community without any network like just you know few random people here and there.
0:4:10.440 --> 0:4:11.180
Karolina | Book Designer
Umm.
0:4:11.660 --> 0:4:19.750
Karolina | Book Designer
And then the pandemic started and I was staying home with with my son and I decided that I don't want to work for someone.
0:4:20.180 --> 0:4:21.810
Karolina | Book Designer
I wanna work for my own.
0:4:21.820 --> 0:4:31.50
Karolina | Book Designer
I want to have the flexibility that it allows me because you know, being immigrants without any family here, we don't have grandparents here.
0:4:31.60 --> 0:4:33.90
Karolina | Book Designer
That kid can take care of our son.
0:4:34.320 --> 0:4:39.890
Karolina | Book Designer
So we we knew that at least one of us and my husband works for for an employer.
0:4:40.120 --> 0:4:50.510
Karolina | Book Designer
We knew that one of us has to have that huge flexibility when it comes, you know, to going and picking my son up from daycare in the middle of the day or taking day off this out of nowhere.
0:4:50.520 --> 0:4:50.830
Karolina | Book Designer
Right.
0:4:51.350 --> 0:4:54.860
Karolina | Book Designer
And we decided that I want to do it anyway.
0:4:55.970 --> 0:4:56.830
Karolina | Book Designer
Umm.
0:5:21.270 --> 0:5:21.410
Emma Bergin
Yeah.
0:4:57.330 --> 0:5:23.70
Karolina | Book Designer
And just it happens that my son was kind of the biggest motivation because I think I wouldn't have the courage to do it in new country that I, you know have known network in and don't know how business works and all that information that you typically have if you're starting a business in, in your own country at least you know to some degree umm.
0:5:32.90 --> 0:5:32.280
Emma Bergin
Yeah.
0:5:23.420 --> 0:5:39.280
Karolina | Book Designer
So I don't think I would have the courage if it wouldn't be for my son, but at the same time it was much harder starting a business having a baby by your side and having the pandemic and being locked and sitting at home.
0:5:46.780 --> 0:5:47.60
Emma Bergin
Right.
0:5:39.840 --> 0:5:59.460
Karolina | Book Designer
So it's it was just a lot of factors that made it very difficult to start and made it feel very lonely because like you know what, when I was starting out, I was just looking for my clients online because, you know, where would I meet them if no in person events were happening?
0:6:0.170 --> 0:6:4.650
Karolina | Book Designer
Umm, yeah, so this is this is basically how how it started.
0:6:5.410 --> 0:6:6.350
Emma Bergin
Ohh, that's awesome.
0:6:6.360 --> 0:6:7.90
Emma Bergin
That's quite the journey.
0:6:8.20 --> 0:6:8.340
Karolina | Book Designer
Yeah.
0:6:9.540 --> 0:6:10.240
Emma Bergin
So. Umm.
0:6:10.160 --> 0:6:12.100
Karolina | Book Designer
Now when I look back, it's like I I can see.
0:6:12.110 --> 0:6:12.810
Karolina | Book Designer
Like what?
0:6:13.200 --> 0:6:13.530
Karolina | Book Designer
How?
0:6:14.90 --> 0:6:16.340
Karolina | Book Designer
And maybe that's why.
0:6:16.140 --> 0:6:16.360
Emma Bergin
Yeah.
0:6:16.790 --> 0:6:20.50
Karolina | Book Designer
Maybe maybe a little stupid to do it this way.
0:6:21.730 --> 0:6:22.780
Emma Bergin
Yeah, it sound.
0:6:22.790 --> 0:6:23.500
Emma Bergin
No, that's awesome.
0:6:25.170 --> 0:6:25.370
Karolina | Book Designer
Yeah.
0:6:23.510 --> 0:6:27.570
Emma Bergin
It's very bold and a lot of people wouldn't take that chance.
0:6:27.580 --> 0:6:28.330
Emma Bergin
So that's really awesome.
0:6:29.620 --> 0:6:29.820
Karolina | Book Designer
Yeah.
0:6:29.610 --> 0:6:31.800
Emma Bergin
So how's everything going now?
0:6:31.890 --> 0:6:33.140
Emma Bergin
Like, how's your business?
0:6:33.150 --> 0:6:36.740
Emma Bergin
Is it still just you by yourself or do you have any employees?
0:6:37.700 --> 0:6:38.330
Emma Bergin
How's that going?
0:6:44.20 --> 0:6:44.260
Emma Bergin
Good.
0:6:46.490 --> 0:6:46.710
Emma Bergin
Umm.
0:6:39.670 --> 0:7:2.560
Karolina | Book Designer
So so I'm a little bit over two years now in the well working full time in the business because once still when I was taking care of my son that was most full time thing to do and I was just, you know, trying to build my website, trying to get some some clients in the evenings whenever I have some spare time.
0:7:3.500 --> 0:7:13.670
Karolina | Book Designer
And once my son was two years old and went to full time to daycare, this is when I actually put focus full time on the business.
0:7:14.610 --> 0:7:16.390
Karolina | Book Designer
So it was a little bit over two years ago.
0:7:16.580 --> 0:7:23.880
Karolina | Book Designer
Umm and I'm I've I've grown since then as a person and the business has grown too.
0:7:25.800 --> 0:7:26.910
Karolina | Book Designer
And I'm still.
0:7:26.920 --> 0:7:27.850
Karolina | Book Designer
It's only me.
0:7:38.250 --> 0:7:38.520
Emma Bergin
Yep.
0:7:28.0 --> 0:7:47.770
Karolina | Book Designer
Uh, for now, however, I'm starting to grow my network, also with with other book designers and some other professionals, and I will be starting to outsource some some work and collaborate on on some project at some point.
0:7:47.780 --> 0:7:49.960
Karolina | Book Designer
Pretty soon. Umm.
0:7:50.480 --> 0:7:51.830
Karolina | Book Designer
So yeah, for now it's still.
0:7:51.840 --> 0:7:57.160
Karolina | Book Designer
It's still me, but it's growing and it's going in the right area direction.
0:7:57.950 --> 0:7:59.60
Emma Bergin
Yeah, that's awesome.
0:7:59.400 --> 0:8:9.760
Emma Bergin
And just in terms of the business like do you have any kind of like really big lessons that you've learned or really significant challenges that you've overcome that you can think of?
0:8:11.20 --> 0:8:12.810
Karolina | Book Designer
Umm, I think you know.
0:8:12.430 --> 0:8:16.350
Emma Bergin
I mean, obviously other than being a full time mom and a full time business owner.
0:8:17.430 --> 0:8:25.820
Karolina | Book Designer
I think that after you know it's with entrepreneurship, it's like every week you're learning something new and and something big.
0:8:27.760 --> 0:8:34.650
Karolina | Book Designer
I think like one of the biggest lessons and at the same time challenges that I had and I had overcome.
0:8:35.320 --> 0:8:46.230
Karolina | Book Designer
Umm was meeting new people and just going out there and being bald about what I do in my business and what I what I can offer to to people.
0:8:59.550 --> 0:8:59.750
Emma Bergin
Umm.
0:8:47.480 --> 0:9:0.990
Karolina | Book Designer
Umm, because you know, starting starting in the pandemic and without any it's it's it's much harder to meet people over the Internet.
0:9:1.40 --> 0:9:10.630
Karolina | Book Designer
And after pandemic and you know, everyone was kind of what became a little bit more introvert than before.
0:9:11.740 --> 0:9:12.80
Emma Bergin
Right.
0:9:11.440 --> 0:9:19.310
Karolina | Book Designer
So it was very hard for me to just, you know, go out and start to meet people and say, hey, I design books, right?
0:9:19.810 --> 0:9:19.970
Emma Bergin
Yeah.
0:9:19.540 --> 0:9:30.870
Karolina | Book Designer
So that was one of the biggest challenges, but also at the same time, one of the biggest learning when I when I when I actually started to do it, I forced myself to get out of my comfort zone and and to do it.
0:9:31.710 --> 0:9:36.650
Karolina | Book Designer
I also saw like a huge value in it and.
0:9:36.770 --> 0:9:36.930
Emma Bergin
Yeah.
0:9:45.260 --> 0:9:45.490
Emma Bergin
Umm.
0:9:38.230 --> 0:9:54.900
Karolina | Book Designer
Not only you know in terms of of getting clients and getting people that will refer you to other people, but just to have that community of like minded and runners that goes through the same things that you are going as an entrepreneur you can share with them.
0:9:54.960 --> 0:9:59.920
Karolina | Book Designer
You can learn and just you know that you have the support that that you need.
0:10:0.570 --> 0:10:1.140
Emma Bergin
Yeah.
0:10:1.210 --> 0:10:2.140
Emma Bergin
Yeah, that's awesome.
0:10:2.610 --> 0:10:15.670
Emma Bergin
And did you always envision kind of like working for yourself and starting something, or was that kind of something that just came with moving and kind of being unsure but your thoughts?
0:10:14.950 --> 0:10:18.970
Karolina | Book Designer
No, I I've never been an employee type.
0:10:19.680 --> 0:10:19.880
Emma Bergin
Yeah.
0:10:20.820 --> 0:10:45.450
Karolina | Book Designer
I think the longest that I've worked for a company was about a year and because I do get bored pretty quickly and I do love wearing all the hats that I need to when I'm working for myself so that that's the one thing that I was in the type of an employee and I always knew that I wanted to work for myself.
0:10:45.560 --> 0:10:49.580
Karolina | Book Designer
Also, my parents, they had their own business.
0:10:50.910 --> 0:10:51.120
Emma Bergin
Umm.
0:10:49.590 --> 0:10:56.460
Karolina | Book Designer
They were entrepreneurs, so I grew up staying how this looks like and this was like the most natural way for me to work.
0:10:57.40 --> 0:10:57.240
Emma Bergin
Yep.
0:10:57.70 --> 0:11:0.730
Karolina | Book Designer
Uh, yeah, because this is this was they, they models that I had.
0:11:16.820 --> 0:11:17.150
Emma Bergin
Hmm.
0:11:1.430 --> 0:11:17.910
Karolina | Book Designer
Umm, so I knew that I want to do it the same way I I want to work on my own terms and I did have a little bit of experience with that before coming to Canada because I had my own business back in Poland for years.
0:11:19.360 --> 0:11:28.120
Karolina | Book Designer
Uh, but like doing it for the second time in in different setting and being much older and much wiser than I did the first time.
0:11:28.770 --> 0:11:37.340
Karolina | Book Designer
Umm, I can see how many mistakes I've I've done then and I know that I wouldn't keep the.
0:11:37.390 --> 0:11:39.420
Karolina | Book Designer
I wouldn't be able to keep the business back then.
0:11:41.230 --> 0:11:45.740
Karolina | Book Designer
Because like the, the reason I I closed the business was because we went to travel with my husband.
0:11:50.770 --> 0:11:51.50
Emma Bergin
Right.
0:11:45.750 --> 0:11:53.330
Karolina | Book Designer
So I I I closed the business, but I was still doing the freelance gigs that that were part of the of the business.
0:11:54.210 --> 0:12:13.60
Karolina | Book Designer
Umm yeah, but it's I could see like, how how many mistakes and like how the whole approach that I had for having my own business wouldn't be sustainable and just wouldn't work in in long term.
0:12:13.790 --> 0:12:22.180
Karolina | Book Designer
Umm, so I kind of had to learn it from scratch all over again because I I knew I didn't do it well.
0:12:22.190 --> 0:12:28.740
Karolina | Book Designer
The for the first time and I'm I'm proud to say that I think I'm doing it right this time. So.
0:12:29.550 --> 0:12:31.640
Emma Bergin
Yeah, that's awesome.
0:12:32.130 --> 0:12:43.100
Emma Bergin
And I know you mentioned this a little bit before you said when you first moved to Canada, you like didn't really make that many relationships, but now you've been kind of focusing on building your network.
0:12:47.900 --> 0:12:48.100
Karolina | Book Designer
Umm.
0:12:43.110 --> 0:12:56.250
Emma Bergin
And so I think maybe that's a good kind of time to transition to we BC and the program you took with them, it's the I'm gonna pull it up because I always say the long title, wrong Discovery Foundation, Strategic mindset program.
0:12:57.620 --> 0:12:57.910
Karolina | Book Designer
Yeah.
0:12:57.560 --> 0:13:6.580
Emma Bergin
Umm, so has that kind of helped you with like building your network and kind of meeting more people as you grow here?
0:13:7.700 --> 0:13:8.950
Karolina | Book Designer
Yeah, for sure.
0:13:12.810 --> 0:13:13.80
Emma Bergin
Umm.
0:13:10.0 --> 0:13:15.650
Karolina | Book Designer
So this is actually my second program with we BC and 2nd peer Mentoring group.
0:13:15.700 --> 0:13:18.930
Karolina | Book Designer
I did the first one a year ago.
0:13:20.700 --> 0:13:20.940
Emma Bergin
OK.
0:13:18.980 --> 0:13:21.450
Karolina | Book Designer
Previous autumn, umm.
0:13:24.20 --> 0:13:24.200
Emma Bergin
OK.
0:13:21.620 --> 0:13:31.630
Karolina | Book Designer
And that was just the premonitory program and right this one this year it was peer mentoring program plus the workshop about the strategic.
0:13:34.490 --> 0:13:34.670
Emma Bergin
Yeah.
0:13:33.970 --> 0:13:36.110
Karolina | Book Designer
This then a whole name.
0:13:37.160 --> 0:13:50.580
Karolina | Book Designer
Umm, so I kind of had like 2 experience experiences with with we BC programs and because the the first one last year was really great and I decided to to park in in the second one this year.
0:13:51.530 --> 0:13:55.80
Karolina | Book Designer
Umm and the.
0:14:1.80 --> 0:14:1.380
Emma Bergin
Umm.
0:13:55.470 --> 0:14:16.280
Karolina | Book Designer
I think the the first program that I took last year was kind of pivotal for me because that was when I took the program I was I already knew that I have to in order to build the business, I have to build stronger network and start growing my support.
0:14:17.210 --> 0:14:22.400
Karolina | Book Designer
But I was still, I still had internal blogs just to do it.
0:14:22.410 --> 0:14:25.410
Karolina | Book Designer
I knew I had to, but I they couldn't get out of of that blog.
0:15:35.980 --> 0:15:36.230
Emma Bergin
Umm.
0:14:26.140 --> 0:15:45.560
Karolina | Book Designer
And what happened during the UM, the mentorship program was that we, we all we're all we all felt safe and very comfortable to share and to be vulnerable uh in in in the group and to share like our biggest you know blogs and issues and and problems so I I went I went pretty deep into my internal blogs and import imposter syndrome and all all this stuff that was happening internally we we didn't meet that wasn't actually like you know and the business thing that that I was facing and all the all the conversation that I had with with other entrepreneurs and all the support that I got from them helped me to start working on my you know internally working on on my blogs and helped me to to all it was a process that took some time but it it ended with me being much more confident about my skills my business and being able to actually start rolling the network and finding the client and it's it's funny because once I.
0:15:47.870 --> 0:15:57.560
Karolina | Book Designer
Once I kind of got through the process and was OK with with me telling everyone about what I do and what I author.
0:15:58.240 --> 0:16:4.350
Karolina | Book Designer
Umm, I don't know is it was kind of like magical because like people started to find me by themselves.
0:16:4.930 --> 0:16:5.210
Emma Bergin
Ah.
0:16:4.360 --> 0:16:10.750
Karolina | Book Designer
It wasn't like by my outrage, but but it it kind of like I've opened myself for it.
0:16:12.0 --> 0:16:12.140
Emma Bergin
Yeah.
0:16:10.760 --> 0:16:12.960
Karolina | Book Designer
And it just, you know, started to come.
0:16:12.970 --> 0:16:16.50
Karolina | Book Designer
So that was one thing.
0:16:16.60 --> 0:16:28.110
Karolina | Book Designer
And this time it was a little bit different like the the formula was a little bit different of the group, but still I got like, I've met great, great people.
0:16:28.120 --> 0:16:37.650
Karolina | Book Designer
I've got a lot of feedback, support and umm yeah, this these programs are really amazing and you can get a lot out of it.
0:16:38.660 --> 0:16:49.650
Emma Bergin
At ourselves and just in terms of kind of like the feedback that you received, like during the programs and what kind of feedback did you get from like the other business owners?
0:16:49.660 --> 0:16:55.260
Emma Bergin
And did you like end up implementing all that feedback into whatever the feedback was based off of?
0:16:56.130 --> 0:16:56.420
Karolina | Book Designer
Yeah.
0:16:56.430 --> 0:17:2.700
Karolina | Book Designer
So. So that first first group I got like one.
0:17:9.430 --> 0:17:9.790
Emma Bergin
Hmm.
0:17:2.710 --> 0:17:12.980
Karolina | Book Designer
I got a lot of advice on the all the internal blogs, imposter syndrome and all that which you know, it wasn't that.
0:17:16.20 --> 0:17:16.240
Emma Bergin
Sorry.
0:17:12.990 --> 0:17:17.900
Karolina | Book Designer
It's not something that you implement straight away, it's something that sits with you and your go through the process.
0:17:19.880 --> 0:17:20.900
Karolina | Book Designer
But I did.
0:17:20.980 --> 0:17:41.110
Karolina | Book Designer
I had like some marketing ideas from from that that I I wasn't thinking about earlier that later I implemented implemented in my business and this time with the group when I was doing the program I was redoing my whole website and adding some new offering.
0:18:5.510 --> 0:18:5.650
Emma Bergin
Yeah.
0:17:41.900 --> 0:18:6.390
Karolina | Book Designer
So I I wanted to, I wanted to get the feedback on the website and the operatings and all that from the group and I got like a lot of great insides that I didn't implement that on the website because getting when you're doing website and you're thinking they copy and everything, you're thinking that you know this is it, it sounds good and and it will be.
0:18:7.70 --> 0:18:7.550
Karolina | Book Designer
Umm.
0:18:8.290 --> 0:18:10.200
Karolina | Book Designer
It will be nice to bring some clients.
0:18:10.210 --> 0:18:17.40
Karolina | Book Designer
Based on that, you don't know until you you know you don't have that fresh perspective of someone, someone else.
0:18:17.50 --> 0:18:24.570
Karolina | Book Designer
So getting a lot of eyes on it and a lot of feedback from different people with different background was very helpful.
0:18:25.380 --> 0:18:26.630
Emma Bergin
Yeah, that's awesome.
0:18:27.20 --> 0:18:37.770
Emma Bergin
And then anything else you wanted to add in terms of your, the programs that you've already taken or maybe like anything, any growth that you've experienced since taking the programs?
0:18:39.370 --> 0:18:40.80
Karolina | Book Designer
UM.
0:18:42.450 --> 0:18:43.140
Karolina | Book Designer
Well, yeah.
0:18:43.150 --> 0:18:59.510
Karolina | Book Designer
Well, the the growth is obvious, but since like since the first the first program that I took it, it was the starter of of the ALDI processes that I had to go through in order to to gain my confidence and and be able to.
0:19:1.740 --> 0:19:4.50
Karolina | Book Designer
Get more attention to to my business.
0:19:4.390 --> 0:19:10.480
Karolina | Book Designer
Umm, so that was I believe that was like very important moment.
0:19:10.490 --> 0:19:18.580
Karolina | Book Designer
And yeah, and it it this was what allowed me to to grow and to be.
0:19:21.260 --> 0:19:26.380
Karolina | Book Designer
To to be in the business like you know which which whole meat, right.
0:19:26.390 --> 0:19:31.20
Karolina | Book Designer
Not just part of it, but yeah, to be the in the business and and be proud of it.
0:19:31.740 --> 0:19:32.990
Emma Bergin
Yeah, that's awesome.
0:19:33.860 --> 0:19:34.470
Emma Bergin
OK.
0:19:34.480 --> 0:19:39.770
Emma Bergin
Well, we can kind of jump on to the next section which talks a little bit about your future.
0:19:39.780 --> 0:19:43.700
Emma Bergin
So and kind of like 2 questions there.
0:19:43.710 --> 0:19:52.400
Emma Bergin
The first one is do you plan to kind of advance and do anymore of the other we BC programs and then kind of like what's next for you?
0:19:54.650 --> 0:19:56.400
Karolina | Book Designer
Umm, what's next for me?
0:19:56.460 --> 0:20:1.260
Karolina | Book Designer
So I plan next year I plan to.
0:20:3.610 --> 0:20:4.230
Karolina | Book Designer
I plan to.
0:20:4.490 --> 0:20:15.990
Karolina | Book Designer
Of course I plan to grow and to to scale the business, to be able to hire some people just to to help me with the things that I'm not the biggest fan of in in the business.
0:20:16.710 --> 0:20:17.540
Karolina | Book Designer
Umm.
0:20:17.690 --> 0:20:23.460
Karolina | Book Designer
And just get more clients, I think to be able to do that.
0:20:36.490 --> 0:20:36.610
Emma Bergin
Yeah.
0:20:25.20 --> 0:20:45.270
Karolina | Book Designer
And in terms of programs, I I watch, I follow we BC and I get their newsletter and I always look for some interesting programs that they have anything new and they if there will be something that I will feel it suits my needs at the moment, then I will surely so with.
0:20:46.80 --> 0:20:47.190
Emma Bergin
Awesome, cool.
0:20:47.820 --> 0:21:2.140
Emma Bergin
And then just in terms of like BC and like building a community, do you feel like right now with the clients that you work with like you're working with the community or helping the community in any way and and if not, that's totally fine.
0:21:2.150 --> 0:21:4.970
Emma Bergin
Like if your clients are all overseas and that's OK too.
0:21:4.980 --> 0:21:6.960
Emma Bergin
But yeah, what are your thoughts there?
0:21:9.690 --> 0:21:20.150
Karolina | Book Designer
Most of my clients like basically 50% of my clients are local from BC and the rest is in US.
0:21:25.910 --> 0:21:26.130
Emma Bergin
Right.
0:21:21.220 --> 0:21:48.460
Karolina | Book Designer
Umm so I I would say it's mix of both because all of my BC clients are they they wanna work with someone who is local even though we communicate, you know over the Internet we usually don't see each other at all because there is no need to umm, it's still important for them to to work with with someone who locale.
0:21:48.610 --> 0:22:1.420
Karolina | Book Designer
And it's also important for me and whenever I need to do some printing or umm, any any other services that I need for my business.
0:22:8.710 --> 0:22:8.850
Emma Bergin
Yeah.
0:22:1.430 --> 0:22:9.810
Karolina | Book Designer
I also go local and I don't you know, I don't outsource things into like Asia or somewhere.
0:22:10.20 --> 0:22:10.950
Karolina | Book Designer
I try.
0:22:10.960 --> 0:22:11.630
Karolina | Book Designer
Yeah, I do.
0:22:11.640 --> 0:22:12.690
Karolina | Book Designer
I do that, but probably too.
0:22:12.700 --> 0:22:16.930
Karolina | Book Designer
So this I would say that this this is the way to to support it.
0:22:17.770 --> 0:22:18.490
Emma Bergin
Yeah.
0:22:18.530 --> 0:22:19.840
Emma Bergin
OK, that's a great answer.
0:22:20.170 --> 0:22:22.820
Emma Bergin
And then this isn't the kind of last question.
0:22:22.830 --> 0:22:24.980
Emma Bergin
But then I'll go back and see if there's anything we missed.
0:22:25.470 --> 0:22:30.810
Emma Bergin
Is that if you were to give advice for anyone who wanted to start their own business, what advice would you give?
0:22:32.420 --> 0:22:36.540
Karolina | Book Designer
Umm, I would say to that.
0:22:36.550 --> 0:22:54.540
Karolina | Book Designer
It's it's really important to have the network and the support and community behind you because it's not only, you know, even if you're not getting clients from, from, from that network or that support having like minded people that you can.
0:22:56.670 --> 0:23:3.860
Karolina | Book Designer
You can bounce your ideas off or just get advice or talk through some.
0:23:4.120 --> 0:23:14.40
Karolina | Book Designer
Some of the challenges you're facing that's that's the one thing I would I would, I would like me to do it sooner.
0:23:15.840 --> 0:23:30.10
Karolina | Book Designer
It's I I was very hesitant about it and it just took me much longer to to come to the place where I'm at now with the business because I was hesitant to do it.
0:23:30.320 --> 0:23:30.490
Emma Bergin
Yeah.
0:23:40.270 --> 0:23:40.490
Emma Bergin
Yeah.
0:23:30.50 --> 0:23:42.200
Karolina | Book Designer
I know that if I would start at the very beginning, I would be, I would be, you know, in in total different place like so that that would be that one piece of advice.
0:23:43.580 --> 0:23:43.920
Emma Bergin
Awesome.
0:23:52.470 --> 0:23:52.690
Emma Bergin
Yeah.
0:23:43.790 --> 0:23:57.950
Karolina | Book Designer
If, if if your intuition tells you that this is something that will help you grow the business, and it probably is, and you should listen to it and not just, you know, not just say dude, dude, would your brain that. No.
0:23:57.960 --> 0:23:59.560
Karolina | Book Designer
No, that's I don't want to do it.
0:23:59.570 --> 0:24:0.710
Karolina | Book Designer
So let's not do it.
0:24:1.370 --> 0:24:2.960
Emma Bergin
Yeah, it's hard to know which is.
0:24:2.970 --> 0:24:4.600
Emma Bergin
Uh, which is the right path to take?
0:24:4.610 --> 0:24:7.270
Emma Bergin
It's a lot of decisions to make, I'm sure.
0:24:7.890 --> 0:24:8.30
Karolina | Book Designer
Yeah.
0:24:9.240 --> 0:24:10.310
Emma Bergin
OK, well.
0:24:9.610 --> 0:24:15.710
Karolina | Book Designer
Yeah, but I think like the the intuition piece is I'm saying that it's for me.
0:24:15.720 --> 0:24:16.990
Karolina | Book Designer
It's it's a big piece.
0:24:17.0 --> 0:24:21.430
Karolina | Book Designer
Whenever my intuition tells me something and I follow it, it it works as I want.
0:24:21.480 --> 0:24:29.220
Karolina | Book Designer
If if my intuition tells me you know, don't do it and I will go with it anyway, usually that wasn't good decision.
0:24:29.230 --> 0:24:31.730
Karolina | Book Designer
So I would say that listen to your garden, yeah.
0:24:31.610 --> 0:24:34.140
Emma Bergin
Yeah, yeah, I love that.
0:24:34.770 --> 0:24:35.220
Emma Bergin
OK.
0:24:35.230 --> 0:24:38.700
Emma Bergin
Well, we only have a few minutes left, so I usually leave a few minutes.
0:24:38.710 --> 0:24:46.660
Emma Bergin
If there's anything else we missed, some people like to like, shout out someone who is really helped them, or an award.
0:24:46.670 --> 0:24:50.860
Emma Bergin
Or just any milestones that you're really excited about.
0:24:50.870 --> 0:24:54.310
Emma Bergin
So yeah, just adding, if there's anything we didn't cover.
0:24:55.700 --> 0:24:58.370
Karolina | Book Designer
Umm, I don't think so.
0:24:58.380 --> 0:25:4.110
Karolina | Book Designer
I like if if I would do a shout out, that would have to include like so many people.
0:25:4.840 --> 0:25:5.0
Emma Bergin
Yeah.
0:25:4.240 --> 0:25:12.240
Karolina | Book Designer
So I would just gave like you know, a shout out to, to to my community of entrepreneurs that that helped me to.
0:25:13.370 --> 0:25:17.210
Karolina | Book Designer
Uh to grow both in business and as a person.
0:25:18.470 --> 0:25:18.970
Emma Bergin
Good.
0:25:19.490 --> 0:25:20.260
Emma Bergin
That's awesome.
0:25:20.830 --> 0:25:22.990
Emma Bergin
OK, well, I'm gonna go ahead and stop the recording.
'''

# Run the pipeline on the example text
#run_pipeline(example_text)
