from crewai_tools import BaseTool

import docx
import re
import json
import docx

def remove_timestamps(text: str) -> str:
    '''
     Function to remove the time stamps from the transcript
    
    '''
    # return re.sub(r'\d{1,2}:\d{2}:\d{2}', '', text)
    return re.sub(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+', '', text)

def remove_extra_spaces(text: str) -> str:
    '''
    Remove the extra spaces from the transcript 
    
    '''
    # return re.sub(r'\s+', ' ', text).strip()
    return re.sub(r'\s+', ' ', text)

def convert_to_json(text: str) -> dict:
    '''
     
    Convert it to json  
    '''
    # lines = text.split('\n')
    # conversation = {'interviewer': [], 'interviewee': []}
    # current_speaker = None
    #
    # for line in lines:
    #     line = line.strip()
    #     if line.startswith('Interviewer:'):
    #         current_speaker = 'interviewer'
    #         conversation[current_speaker].append(line.replace('Interviewer:', '').strip())
    #     elif line.startswith('Interviewee:'):
    #         current_speaker = 'interviewee'
    #         conversation[current_speaker].append(line.replace('Interviewee:', '').strip())
    #     elif current_speaker:
    #         conversation[current_speaker].append(line)
    #
    # # Convert lists to single strings
    # conversation['interviewer'] = ' '.join(conversation['interviewer'])
    # conversation['interviewee'] = ' '.join(conversation['interviewee'])
    #
    # return conversation
    lines = text.split('\n')  # Split by newline
    extracted_lines = []
    timestamp_pattern = re.compile(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+')
    for line in lines:
        if not timestamp_pattern.match(line.strip()):
            extracted_lines.append(line.strip())
    lines = extracted_lines
    l = []
    i = 0
    while i < len(lines):
        if lines[i] == '':
            i += 1
            continue

        new_dict = {}
        key = lines[i]
        value = lines[i + 1]
        new_dict[key] = value
        l.append(new_dict)
        i += 2  # Move to the next key-value pair

    with open('output2.json', 'w') as f:
        json.dump(l, f, indent=4)

    return dict(l)