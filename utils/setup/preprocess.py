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

So I guess just to start simply kind of what you were doing before you owned cloudmine software kind of your career journey, if you wanna walk me through that and then we can go into your business now.
0:0:14.810 --> 0:0:15.340
Monica Tsai
Sure.
0:0:15.400 --> 0:0:21.320
Monica Tsai
Uh prior to clot, mine really spend the last 1520 years being in HR professional.
0:0:21.570 --> 0:0:33.220
Monica Tsai
So I graduating from school was a psychology degree really didn't know what I wanted to do, and people were just saying, well, you know, maybe try this, maybe try that and somehow HR resonated with me.
0:0:33.230 --> 0:0:51.450
Monica Tsai
So I went in and started a certificate program with BCIT and got lucky enough to also have an opportunity working in an engine, consulting engineering company and kind of that's how I my HR career started really didn't know much about like what does HHR do you know?
0:0:51.460 --> 0:0:56.510
Monica Tsai
Like what was the exception of knowing that not a lot of people like HR department?
0:0:56.520 --> 0:0:58.230
Monica Tsai
That's probably my first impression.
0:0:58.540 --> 0:1:2.450
Monica Tsai
And then little did I know how much I actually enjoyed it.
0:1:2.700 --> 0:1:9.690
Monica Tsai
It wasn't so much just the opportunity to talk to different people and also learn about what everybody's story is about.
0:1:9.900 --> 0:1:21.420
Monica Tsai
It was really about knowing that keeping that relationship going and connection really can help to Megan or organization or working environment, a great place to be, you know.
0:1:29.450 --> 0:1:29.720
Emma Bergin
Umm.
0:1:21.430 --> 0:1:34.670
Monica Tsai
And given that I am a gamer, a video gamer myself, I've always wanted to work for a video gaming company and knowing that I probably wouldn't want to go back to school studying like computing science or whatnot.
0:1:34.790 --> 0:1:39.320
Monica Tsai
I just thought that, well, maybe HR can somehow go into a video gaming.
0:1:39.330 --> 0:2:3.360
Monica Tsai
So I had the opportunity to work for Disney Interactive Studio when I had a studio in Vancouver and then I kind of embark my journey on the in the tech industry ever since ever I said ever since I got into the industry, I really enjoyed the environment, the flexibility and how quickly things are going and really found myself thinking that, well, that is really cool.
0:2:3.370 --> 0:2:25.820
Monica Tsai
Being able to like create something from the ground up, I had the opportunity of not just observing people doing that, but also helping some aspect of project, specifically game projects to launch the how it can be and that's how I kind of discover I really enjoy creative creating things like the creative side of things.
0:2:26.430 --> 0:2:33.760
Monica Tsai
I can do the maintenance part in terms of hey, when something's on track and keep it, keep it going and whatnot, I can do that.
0:2:33.870 --> 0:2:38.680
Monica Tsai
If I have a choice, I'd rather be creating stuff and that's where I kind of thought about.
0:2:38.690 --> 0:2:57.530
Monica Tsai
Well, maybe just maybe, you know, I could start a company and so let my last in House position as an HR person a couple years ago and started my own consulting mostly because it was my way of still being in touch in HR.
0:3:1.400 --> 0:3:1.640
Emma Bergin
Umm.
0:2:57.540 --> 0:3:9.360
Monica Tsai
I didn't quite feel like my chapter in HR had closed, and so that's where I continue doing some HR consulting at the same time, not allow me the flexibility of finishing my degree.
0:3:9.370 --> 0:3:13.400
Monica Tsai
So I am right now finishing my doctoral degree in social science.
0:3:14.120 --> 0:3:14.500
Emma Bergin
Wow.
0:3:14.130 --> 0:3:22.280
Monica Tsai
I've always been working and learning at the same time and that's how I got my masters in leadership.
0:3:22.290 --> 0:3:25.920
Monica Tsai
And then various different certifications and whatnot.
0:3:25.970 --> 0:3:34.880
Monica Tsai
And then also formal degree in doctoral I'm about to defend my doctoral, which is really exciting because it's been a long journey to come.
0:3:35.380 --> 0:3:44.700
Monica Tsai
At the same time, it also kept me in touch with the intellectual side of myself being able to just exercise my brain slightly differently in that regard.
0:3:44.710 --> 0:3:48.520
Monica Tsai
And that's what brought us today up to Cloudmind.
0:3:48.530 --> 0:3:57.940
Monica Tsai
So as I was starting my consulting career, I was also thinking about, well, what are the possibility of branching out something else aside from just being HR.
0:3:57.950 --> 0:4:1.400
Monica Tsai
I know that HR is my bread and butter at the same time.
0:4:1.410 --> 0:4:15.300
Monica Tsai
I really enjoy software development, so I've been fortunate enough to work with smart people as well as partner was really, really, really talented individuals to build different softwares and cloudline.
0:4:15.350 --> 0:4:35.930
Monica Tsai
Our focus is to build a digital companion that will give people some companionship in a way our first product is going to focus on elder care, specifically, people who are experiencing or maybe experiencing memory loss, dementia, Alzheimer's, so on so forth.
0:4:35.940 --> 0:4:37.120
Monica Tsai
So that's our first product.
0:4:37.370 --> 0:5:18.980
Monica Tsai
Where our focus is going to be, it's been about outside about 8 months since we embarked on actually developing a proof of concept, and currently we do have a proof of concept software that is still being enhanced and worked on and in the process of really branching out to network and getting to know the people within the industry, specifically elder care and things like that, because that's an industry that I have no prior knowledge or prior experience in knowing that I've been in video gaming, if you if I were to build a video game, it would happen so much easier and I still have passion for it.
0:5:24.960 --> 0:5:25.120
Emma Bergin
Yeah.
0:5:26.890 --> 0:5:27.140
Emma Bergin
Wow.
0:5:18.990 --> 0:5:29.880
Monica Tsai
Don't get me wrong, I do think that I wanted to make something that can be impactful to a larger group of people, and that's where where our focus happening for cloudmind.
0:5:30.920 --> 0:5:31.530
Emma Bergin
Anything.
0:5:30.30 --> 0:5:32.70
Monica Tsai
Yeah, yeah.
0:5:35.50 --> 0:5:35.230
Monica Tsai
Yeah.
0:5:31.940 --> 0:5:37.470
Emma Bergin
OK, I have a few questions just to make sure I got all the details right.
0:5:37.480 --> 0:5:59.610
Emma Bergin
So it sounds like to me, you initially kind of started your career in HR and then can you just maybe correct me if I'm wrong here, but you worked for a different software companies and that's kind of how you learned a little bit more about like the engineering field and software development and you could created some really great relationships with either like people you were hiring or within the company.
0:5:59.620 --> 0:6:0.150
Emma Bergin
Is that right?
0:6:0.610 --> 0:6:1.330
Monica Tsai
That is correct, yes.
0:6:2.50 --> 0:6:2.870
Emma Bergin
OK, awesome.
0:6:2.880 --> 0:6:8.340
Emma Bergin
So that's kind of what led you to being like, oh, I think I could, you know, start my own company and do this on my own.
0:6:9.10 --> 0:6:9.590
Monica Tsai
Yeah, yeah.
0:6:10.360 --> 0:6:10.780
Emma Bergin
OK, cool.
0:6:12.130 --> 0:6:20.60
Emma Bergin
And then just to go back a little bit, I know you mentioned you had a masters in leadership and then the degree or the doctorate in social science.
0:6:24.140 --> 0:6:24.380
Monica Tsai
Umm.
0:6:28.750 --> 0:6:28.870
Monica Tsai
Yeah.
0:6:20.70 --> 0:6:32.130
Emma Bergin
So do you wanna chat a little bit about why those two things were important to you when it kind of seems like you know you have your HR side and then you have your video game side, so where did those two kind of come from?
0:6:33.720 --> 0:6:59.810
Monica Tsai
I think one of my biggest passion, and this is leadership development and not a lot stem from my interaction, was managers and leaders throughout the years as an HR professional, right is CID amount of challenges, struggles, fulfillment, rewarding moments for a leader, particularly the newer leaders per SE.
0:7:0.120 --> 0:7:5.230
Monica Tsai
And so that's where it really got me into wanting to learn a little bit more about leadership.
0:7:5.240 --> 0:7:12.100
Monica Tsai
And so kind of got myself into the masters program in in leadership with royal roads.
0:7:12.230 --> 0:7:14.460
Monica Tsai
Royally enjoy my time there.
0:7:14.610 --> 0:7:20.250
Monica Tsai
So much so that I originally was like, no, I think I'm good after master's degree in.
0:7:21.260 --> 0:7:31.890
Monica Tsai
A couple weeks after I graduated, I decided to put my application in for a doctoral program and incidentally got into a doctoral program.
0:7:31.900 --> 0:7:37.860
Monica Tsai
It was the first like when I first got the acceptance email, I was something must be wrong.
0:7:37.870 --> 0:7:39.430
Monica Tsai
Like there's something wrong with it.
0:7:39.440 --> 0:7:48.870
Monica Tsai
Like, I don't think it was possible and and to the degree when I was sitting and orientation with other people in the room, I was saying no.
0:7:48.880 --> 0:7:52.160
Monica Tsai
They must have got my name wrong, like I shouldn't be here.
0:7:52.170 --> 0:7:57.960
Monica Tsai
So there's a genuine sense of imposter syndrome, as many people call and.
0:7:58.470 --> 0:8:4.840
Monica Tsai
But really got into knowing, OK why I was chosen because my doctoral thesis is surrounding.
0:8:5.50 --> 0:8:17.260
Monica Tsai
How augmented intelligence would be able to support leaders, particularly in emerging leaders, those are the ones that are transitioning from an individual contributor to a manager or leadership role.
0:8:17.510 --> 0:8:25.720
Monica Tsai
How the tool and the technology may be able to support them through that transition and in the long run for their own personal leadership development.
0:8:48.680 --> 0:8:48.850
Emma Bergin
Yeah.
0:8:26.290 --> 0:8:49.110
Monica Tsai
That really combined the two passions that I have technology specifically AI, Ohh augmented technology and also leadership development together and and not also kind of paved the way of me thinking around building a software that can enhance or help people and even impact hopefully a positive impact in their lives. Yeah.
0:8:49.840 --> 0:8:50.450
Emma Bergin
Amazing.
0:8:50.460 --> 0:8:51.490
Emma Bergin
That's very cool.
0:8:51.660 --> 0:8:52.930
Emma Bergin
I never heard anything like this.
0:8:52.940 --> 0:8:53.950
Emma Bergin
That's really exciting.
0:8:54.340 --> 0:8:54.520
Monica Tsai
Yeah.
0:8:54.230 --> 0:8:57.10
Emma Bergin
And so do you wanna chat through a little bit.
0:9:1.710 --> 0:9:1.950
Monica Tsai
Umm.
0:8:57.20 --> 0:9:2.990
Emma Bergin
So for the software that you're developing for, the elder community, do you wanna chat there a little bit?
0:9:3.0 --> 0:9:4.830
Emma Bergin
Kind of what that would look like.
0:9:5.160 --> 0:9:5.440
Monica Tsai
Umm.
0:9:4.840 --> 0:9:9.270
Emma Bergin
What your plans are maybe for the future and I don't think you mentioned this.
0:9:9.280 --> 0:9:10.250
Emma Bergin
So do you want?
0:9:10.260 --> 0:9:13.300
Emma Bergin
Do you mind just sharing when you started this business as well?
0:9:13.910 --> 0:9:14.480
Monica Tsai
Yeah.
0:9:14.520 --> 0:9:30.280
Monica Tsai
Uh, we sorted out the business back in I think it was May 2022 was when the the business was registered and the idea actually came a little bit earlier, but we decided to me and my business partner decided that, yeah, no, we wanted to do this.
0:9:30.290 --> 0:9:32.220
Monica Tsai
So we registered it and whatnot.
0:9:32.290 --> 0:9:40.600
Monica Tsai
It was kind of be in a download for a little bit until early last year where we're like, no, we really need to start doing something with it.
0:9:41.0 --> 0:9:44.400
Monica Tsai
A couple things that happened during that time chat GPT happened.
0:9:45.90 --> 0:9:45.330
Emma Bergin
Yeah.
0:9:44.930 --> 0:9:49.970
Monica Tsai
That's why and, and we all know how that's been going so far.
0:9:50.390 --> 0:10:0.890
Monica Tsai
And so we were like, OK, now this is getting real and the technology itself is really allowing us the opportunity to make something for it.
0:10:0.950 --> 0:10:6.680
Monica Tsai
And so that kind of gave us a little bit of a push in terms of really doing something with our business.
0:10:6.690 --> 0:10:26.80
Monica Tsai
And then secondly, just the amount of people that we talked to casually about the idea that really resonated with them, the reason why we're focusing on elder care, specifically, people who are experiencing or maybe experiencing memory loss was really started from a personal story from my business partner.
0:10:26.260 --> 0:10:47.590
Monica Tsai
He had some personal experience and and witnessing some personal I'm friends sort of taking care of people who had Alzheimer's or dementia and alike and being able to kind of relay that story thinking now, OK, it's not just the people who are experiencing that memory loss, needing a companion.
0:10:53.520 --> 0:10:53.810
Emma Bergin
Right.
0:10:48.660 --> 0:10:54.660
Monica Tsai
It's also a companion for the people who are giving care for those individuals, right?
0:10:54.670 --> 0:11:11.340
Monica Tsai
Because it can get really lonely and tiresome, particularly for the caregivers, because there can be long days of repeating the same story of listening to the stories repeatedly and still wanting to needing to be patient with an individual because they know no difference.
0:11:11.590 --> 0:11:11.900
Monica Tsai
Right.
0:11:11.890 --> 0:11:12.80
Emma Bergin
OK.
0:11:11.910 --> 0:11:22.50
Monica Tsai
So, and in talking to a lot of people, we we saw that resonated with many individuals out within our network and decide that, yeah, no, this is the right thing to do.
0:11:22.60 --> 0:11:24.30
Monica Tsai
We really want to make an impact for it.
0:11:24.920 --> 0:11:36.930
Monica Tsai
So what we've done since then was creating a video really to showcase the product or sort of our our vision for what it can help, which is on our website.
0:11:36.980 --> 0:11:44.50
Monica Tsai
So I invite you to go to our website and and and watch the video that was about like 3 1/2 minutes or so.
0:11:57.780 --> 0:11:57.990
Emma Bergin
You know.
0:11:44.360 --> 0:12:1.290
Monica Tsai
Really just speaks to what we're intending to build is something that can be accessible and available to an elderly individual when they wake up 3:00 o'clock in the morning confused about where they are, but having a voice, being able to tell them that, hey, it's OK.
0:12:1.400 --> 0:12:2.250
Monica Tsai
You're at home.
0:12:2.680 --> 0:12:3.810
Monica Tsai
I'm here with you.
0:12:4.0 --> 0:12:4.610
Monica Tsai
Tell me.
0:12:4.620 --> 0:12:5.160
Monica Tsai
Let's tell.
0:12:5.170 --> 0:12:17.550
Monica Tsai
Let's talk about things that can come you down that can make sure we can help you back to sleep where you need, and then until somebody else who's able to come in in real life to continue dot care.
0:12:18.180 --> 0:12:18.410
Monica Tsai
Right.
0:12:18.420 --> 0:12:33.120
Monica Tsai
Because it is, I think it's really hard demanding a real life person and human being to be with an elderly individual when they are experiencing dementia and and such 24/7, right?
0:12:33.130 --> 0:12:41.620
Monica Tsai
It's really tiring and they may need some relief, so our goal is to build a digital companion that can help to supplement.
0:12:41.770 --> 0:12:44.660
Monica Tsai
So it's not designed to replace.
0:12:53.990 --> 0:12:54.170
Emma Bergin
Yeah.
0:12:44.710 --> 0:12:54.310
Monica Tsai
It is designed to supplement and be a companion for both the elderly individual as well as their caregivers, so hopefully that give you a little bit better sense.
0:12:54.320 --> 0:12:56.610
Monica Tsai
Interpret what we're trying to building, yeah.
0:12:56.260 --> 0:12:57.180
Emma Bergin
Yeah, that's awesome.
0:12:57.190 --> 0:12:58.330
Emma Bergin
Thank you for all that insight.
0:13:0.310 --> 0:13:0.470
Monica Tsai
Yeah.
0:12:58.340 --> 0:13:1.50
Emma Bergin
I think that makes tons of sense and I'm really excited.
0:13:1.60 --> 0:13:2.60
Emma Bergin
That sounds really awesome.
0:13:2.700 --> 0:13:2.860
Monica Tsai
Yeah.
0:13:3.980 --> 0:13:4.790
Emma Bergin
Hey, great.
0:13:5.480 --> 0:13:7.170
Emma Bergin
And now you mentioned a business partner.
0:13:7.180 --> 0:13:12.420
Emma Bergin
So is it just the two of you right now or do you have on any software developers or people working underneath you?
0:13:11.530 --> 0:13:13.600
Monica Tsai
Umm yeah.
0:13:13.610 --> 0:13:17.640
Monica Tsai
So uh, in the business is really just me and my business partner right now.
0:13:17.650 --> 0:13:24.560
Monica Tsai
We do have it external vendor that we have hired to do the actual building of the proof of concept.
0:13:24.860 --> 0:13:25.120
Emma Bergin
Umm.
0:13:24.950 --> 0:13:31.720
Monica Tsai
So that's where we are right now and the relationship has been going off since I think since June of last year.
0:13:31.730 --> 0:13:48.960
Monica Tsai
So it's been almost eight months right now it's been working out well, but obviously our goal remains to want to build our own internal team and really figure out what that what's going to help us two, at least the first bit of market testing and that's what we're focusing on right now.
0:13:50.50 --> 0:13:50.620
Emma Bergin
Awesome.
0:13:51.50 --> 0:13:51.170
Monica Tsai
Yeah.
0:13:50.910 --> 0:14:3.120
Emma Bergin
And then in the future, do you foresee just in terms of where the product will go, do you think it'll kind of live in retirement homes or be kind of like an individual product you can order online like ordering a laptop?
0:14:6.690 --> 0:14:6.880
Monica Tsai
Yeah.
0:14:3.130 --> 0:14:7.860
Emma Bergin
Like, what's kind of the goal in terms of where it's sold or maybe you don't know yet, which is totally fine.
0:14:8.550 --> 0:14:8.940
Monica Tsai
Yeah.
0:14:17.470 --> 0:14:17.690
Emma Bergin
Yeah.
0:14:8.950 --> 0:14:22.440
Monica Tsai
So our goal is to make sure the accessibility is there, which means that it should be on a mobile device at a minimum, or at least a living as a web application that people can access to using the laptop.
0:14:22.610 --> 0:14:33.400
Monica Tsai
We do tend to focus a little bit more on mobile device because I think if I were to look at my parents, they probably spend much more time on their iPhone or their iPad rather than their laptop.
0:14:33.530 --> 0:14:40.440
Monica Tsai
And that's where I'm kind of getting that gauge in terms of what would make sense and then ease of use, of course.
0:14:40.680 --> 0:14:46.190
Monica Tsai
So that's what we've been focusing on in terms of exactly where that setting is going to be.
0:14:46.260 --> 0:15:9.860
Monica Tsai
We're going into sort of a small deployment phase to do market validation and real user feedback side of things and are we're looking for partners in the retirement living setting who may be able to just give us a little bit more insight or even allow us to have deploy the software to a handful of users to get some real time be back.
0:15:10.30 --> 0:15:21.120
Monica Tsai
One thing that I came to realization is when I'm thinking about the product and how it should go and whatnot, I could never put myself in the shoes of a 75 years old.
0:15:23.530 --> 0:15:23.830
Emma Bergin
Come.
0:15:21.130 --> 0:15:27.70
Monica Tsai
That's that has dementia, or is trying to let engage with a machine, right.
0:15:27.100 --> 0:15:27.380
Emma Bergin
Right.
0:15:33.390 --> 0:15:33.730
Emma Bergin
Right.
0:15:27.130 --> 0:15:33.880
Monica Tsai
I just can't and I haven't had the opportunity to really observe somebody like that aside from my parents.
0:15:33.890 --> 0:15:36.290
Monica Tsai
But, but that's slightly different.
0:15:37.140 --> 0:15:37.320
Emma Bergin
Yeah.
0:15:38.330 --> 0:16:12.790
Monica Tsai
And I I think there is a power to words really seeing that in real life, even if it's just a handful of users and that's what I'm focusing on come this new year, is being able to expand my network and I credit we BC or what for this because of the mentorship program that I was in and being able to get to know other individuals doing other really cool stuff and having that support not just from the mentor but also the people who are involved in the cohort to kind of tossed out different ideas.
0:16:12.800 --> 0:16:18.280
Monica Tsai
And then maybe making some connections as an extension from my connection with them so.
0:16:18.930 --> 0:16:20.20
Emma Bergin
Yeah, that's awesome.
0:16:25.630 --> 0:16:25.800
Monica Tsai
Yeah.
0:16:28.940 --> 0:16:29.80
Monica Tsai
Yes.
0:16:20.30 --> 0:16:31.40
Emma Bergin
And I'm sure it's just super helpful just to have other ideas outside of like you or your business partner because you know it's hard if it's just two people, you know, it's more heads are better than you.
0:16:31.930 --> 0:16:32.440
Monica Tsai
Yes.
0:16:32.450 --> 0:16:33.670
Monica Tsai
Yeah, exactly. Yeah.
0:16:33.890 --> 0:16:35.940
Emma Bergin
OK, well this is a good transition actually.
0:16:35.950 --> 0:16:41.20
Emma Bergin
Do you want to chat through your experience in the Discovery mindset program?
0:16:41.60 --> 0:16:41.320
Monica Tsai
Umm.
0:16:43.250 --> 0:16:43.590
Monica Tsai
Umm.
0:16:41.170 --> 0:16:44.160
Emma Bergin
Maybe why you took it and kind of what you were looking for.
0:16:44.170 --> 0:16:44.480
Emma Bergin
I know.
0:16:46.460 --> 0:16:46.620
Monica Tsai
Yeah.
0:16:50.210 --> 0:16:50.430
Monica Tsai
Umm.
0:16:44.490 --> 0:16:52.0
Emma Bergin
Maybe you just described it a little bit and then walk through kind of any lessons or any takeaways from the program?
0:16:52.670 --> 0:16:53.620
Monica Tsai
Yeah, yeah.
0:16:54.10 --> 0:17:0.750
Monica Tsai
So I stumbled on the program because I was, you know, a big part of who I am is learned.
0:17:0.920 --> 0:17:2.80
Monica Tsai
You're learning right?
0:17:5.80 --> 0:17:5.360
Emma Bergin
Yeah.
0:17:2.350 --> 0:17:9.410
Monica Tsai
As you can see, taking that many degrees and whatnot, and I was like, OK, I don't know how does this gonna work?
0:17:9.420 --> 0:17:10.550
Monica Tsai
I don't understand.
0:17:10.640 --> 0:17:12.930
Monica Tsai
There is not a handbook for entrepreneurs.
0:17:12.940 --> 0:17:15.330
Monica Tsai
How you should start these are the steps to do right.
0:17:15.400 --> 0:17:21.570
Monica Tsai
So I search online and we BC program popped up and I was like, OK, I wonder how this is going to be.
0:17:21.960 --> 0:17:42.250
Monica Tsai
I've been really, really fortunate over the course of my career as an HR person to have a network of individuals say no within the tech industry, and I saw the power of people getting together and being able to just, you know, lean on one another on for ideas, for feedback, for just even a sounding board.
0:17:42.290 --> 0:17:45.960
Monica Tsai
And that's what really drew me towards the mentorship program.
0:17:46.670 --> 0:17:46.840
Emma Bergin
Yeah.
0:17:46.820 --> 0:17:54.390
Monica Tsai
Got myself registered and got lucky to prepare with other individuals within the program or mentor Cassandra.
0:17:54.400 --> 0:17:55.360
Monica Tsai
I don't know whether you can.
0:17:55.420 --> 0:18:1.170
Monica Tsai
You can say her name, but she's been phenomenal in terms of facilitating a conversation.
0:18:1.420 --> 0:18:5.150
Monica Tsai
There have been times where I was traveling and wasn't able to.
0:18:5.220 --> 0:18:25.180
Monica Tsai
Wasn't was having challenges in making the sessions itself, but I always try to make sure that I'm be there because so not just the sort of the wealth of information that came out of the conversation, the amount of connection, the openness that people are willing to share, that was just phenomenal.
0:18:25.450 --> 0:18:47.540
Monica Tsai
And so I got I think even if I'm not the center at the center stage in terms of sharing the challenges that I have just listening and providing my perspective towards other people's challenges, that gave me even more insights towards how I should be thinking about things or other perspectives that I can consider.
0:19:1.960 --> 0:19:2.170
Emma Bergin
Yeah.
0:18:47.650 --> 0:19:3.330
Monica Tsai
And I thought that was just very, very powerful and and to a degree, my assumption is that us all being women in the room also had the power of being vulnerable with one another, being open to one another.
0:19:3.400 --> 0:19:3.650
Monica Tsai
Right.
0:19:3.660 --> 0:19:12.470
Monica Tsai
And I I think that's that's where the value I got out of it is really just the openness and the dialogue that we have within the program.
0:19:12.800 --> 0:19:29.480
Monica Tsai
The biggest lesson that I took away from is just, you know, the connection remains to be important and we we try our best to see after the formal program had concluded whether we can get together on the periodic basis just to provide support and whatnot.
0:19:29.490 --> 0:19:30.560
Monica Tsai
And that's been going on.
0:19:30.570 --> 0:19:47.110
Monica Tsai
And I think that was really one of the key learnings that I took away from is being able to not just listen to other people's challenges and provide perspective being open enough to receive and also see the different perspective as we're having a discussion around that.
0:19:48.100 --> 0:19:49.170
Emma Bergin
Yeah, that's awesome.
0:19:49.180 --> 0:19:50.470
Emma Bergin
Well, thank you for all that.
0:19:50.480 --> 0:19:58.480
Emma Bergin
And do you feel like there was anything that came out of the program that you were able to apply to your business, like any advice or feedback?
0:19:59.390 --> 0:20:0.540
Monica Tsai
Yeah, absolutely.
0:20:0.630 --> 0:20:5.380
Monica Tsai
I think just the the network side of things, right, being able to know.
0:20:5.440 --> 0:20:17.970
Monica Tsai
I other people sued the program, though that we're not all within Lower Mainland and the ones that either had came to Lower Mainland for their personal staff and or people who are in Lower Mainland.
0:20:22.830 --> 0:20:22.950
Emma Bergin
Yeah.
0:20:17.980 --> 0:20:26.810
Monica Tsai
I actually got a chance to meet with a couple of the individuals within the program in person, which was really powerful and really cool to see how you actually looked like this.
0:20:26.820 --> 0:20:30.170
Monica Tsai
You know, this is what you look like without the screen around you.
0:20:30.180 --> 0:20:30.480
Monica Tsai
So.
0:20:30.990 --> 0:20:31.380
Emma Bergin
Hello.
0:20:30.520 --> 0:20:42.60
Monica Tsai
So that was really cool and continuing on those relationships and then then being really open and gracious around offering to expand my network.
0:20:45.140 --> 0:20:45.790
Emma Bergin
Mazing.
0:20:42.70 --> 0:20:46.350
Monica Tsai
I think those were the big takeaways that I got, yeah.
0:20:45.840 --> 0:20:46.890
Emma Bergin
OK, great.
0:20:47.40 --> 0:20:50.90
Emma Bergin
Well, we only have 5 minutes left, so I'm gonna leave some time.
0:20:50.100 --> 0:20:54.750
Emma Bergin
Is there anything I missed or anything else you wanted to add either about your business or the program?
0:20:58.820 --> 0:20:59.0
Emma Bergin
Yeah.
0:20:55.880 --> 0:21:10.490
Monica Tsai
No, no, I think we'll cover a whole ton of grounds and really just very grateful to have the opportunity to kind of share my own story and hopefully encourage others to either participate in the program or share their stories as well.
0:21:11.200 --> 0:21:11.590
Emma Bergin
Yeah.
0:21:11.600 --> 0:21:12.90
Emma Bergin
Awesome.
0:21:12.100 --> 0:21:12.450
Emma Bergin
OK.
0:21:12.460 --> 0:21:15.710
Emma Bergin
And then my last question for you, which is a question I ask everybody.
0:21:16.140 --> 0:21:16.550
Monica Tsai
Umm.
0:21:21.80 --> 0:21:21.340
Monica Tsai
Hmm.
0:21:15.720 --> 0:21:21.550
Emma Bergin
So if you were gonna give advice to someone who wanted to start their own business, what advice would you give?
0:21:23.700 --> 0:21:24.550
Monica Tsai
That's tough one.
0:21:28.400 --> 0:21:38.170
Monica Tsai
I would say be clear on why you're doing this and constantly remind yourself about your why.
0:21:38.710 --> 0:21:38.870
Emma Bergin
Yeah.
0:21:38.470 --> 0:21:40.110
Monica Tsai
I know it sounds very cliche.
0:21:41.390 --> 0:21:42.120
Emma Bergin
I don't like him.
0:21:40.120 --> 0:21:44.10
Monica Tsai
Very Simon Scenic, I think not.
0:21:44.20 --> 0:21:47.810
Monica Tsai
Had got me through days where I was like, what am I doing this like?
0:21:47.820 --> 0:21:55.350
Monica Tsai
This is not fun, yet I often relate back to OK, This is why it's important for me, right?
0:21:55.360 --> 0:21:57.540
Monica Tsai
So go back to my personal value.
0:21:57.550 --> 0:22:4.110
Monica Tsai
Go back to why is it important for me personally, not just for the business?
0:22:4.450 --> 0:22:11.980
Monica Tsai
Because I think the business would not exist if I'm not clear about why it's important for me, then I'm not even motivated to do that.
0:22:12.370 --> 0:22:12.940
Monica Tsai
Alright so.
0:22:12.740 --> 0:22:13.270
Emma Bergin
Yeah.
0:22:13.660 --> 0:22:14.30
Emma Bergin
Yeah.
0:22:14.40 --> 0:22:17.870
Emma Bergin
No, it's just like going back to that connection and your values that makes that makes sense.
0:22:17.880 --> 0:22:18.400
Emma Bergin
That's great advice.
0:22:17.280 --> 0:22:19.220
Monica Tsai
Yeah, yeah, yeah.
0:22:20.370 --> 0:22:21.50
Emma Bergin
OK.
0:22:21.170 --> 0:22:23.460
Emma Bergin
Well, that's it from me.
0:22:23.910 --> 0:22:25.650
Emma Bergin
I'm gonna go ahead and stop the recording.
0:22:26.250 --> 0:22:26.440
Monica Tsai
OK.
'''

# Run the pipeline on the example text
# run_pipeline(example_text)
