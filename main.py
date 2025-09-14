import parser
import processor



if __name__ == "__main__":

    # Eventually, consume URLs from a Kafka topic

    # For now, consume a single hard-coded URL
    url = "https://www.lockheedmartinjobs.com/job/littleton/software-engineer-sr-cyber-ts-sci-clearance/694/81191846592"
    dataObj = parser.parse_url(url)

    # print(f"Job Title: {dataObj.job_title}")
    # print()
    # print(f"Job Description: {dataObj.job_description}")

    section_text = "Basic Qualifications:"
    qualsIndex = processor.find_index_of_section_test(dataObj.job_description_tokens, section_text)
    print(f"Index of {section_text} text: {qualsIndex}")

    section_text = "Desired Skills:"
    beforeSkillsIndex = processor.find_index_of_section_test(dataObj.job_description_tokens, section_text, True)
    afterSkillsIndex = processor.find_index_of_section_test(dataObj.job_description_tokens, section_text)

    print(f"Index of {section_text} text: {afterSkillsIndex}")

    section_text = "Security Clearance Statement:"
    finalIndex = processor.find_index_of_section_test(dataObj.job_description_tokens, section_text, True)
    print(f"Index of {section_text} text: {finalIndex}")

    print(f"Basic Qualifications text: \n\n {dataObj.job_description_tokens[qualsIndex:beforeSkillsIndex]}")
    print('\n\n')
    print(f"Desired Skills text: \n\n {dataObj.job_description_tokens[afterSkillsIndex:finalIndex]}")
