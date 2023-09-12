import re

list_EI = []
counterEIA = 0
counterEIB = 0

list_SN = []
counterSNA = 0
counterSNB = 0

list_JP = []
counterJPA = 0
counterJPB = 0

list_TF = []
counterTFA = 0
counterTFB = 0

user_name = " "
personalityOutput = " "


def first():
    global user_name
    user_name = input("What is your name:\n ")
    print("1) A. Expend energy, enjoy groups.       B. Conserve energy, one-on-one\n")
    user_entry = input("Enter A or B: ")
    global list_EI
    global counterEIA
    global counterEIB

    ans = "A"
    answer = "B"
    if user_entry.casefold() == ans.casefold():
        list_EI.append("A. Expend energy, enjoy groups")
        counterEIA += 1
        second()
    elif user_entry == answer.casefold():
        list_EI.append(" B. Conserve energy, one-on-one")
        counterEIB += 1
        second()
    else:
        print("""   
                Expected A or B as response
                I know this is an error, please try again""")
        first()


def second():
    print("2) A. Interpret literally.         B. Look for meaning and possibilities.\n")
    user = input("Enter A or B: ")
    global list_EI
    global counterEIA
    global counterEIB
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_EI.append("A. Interpret literally.")
        counterEIA += 1
        third()
    elif user.casefold() == answer.casefold():
        list_EI.append("B. Look for meaning and possibilities.")
        counterEIB += 1
        third()
    else:
        print("""        
                Expected A or B as response
                I know this is an error, please try again""")
        second()


def third():
    print("3) A. Logical, thinking, questioning.          B. Empathetic, feeling, accommodating.\n")
    user = input("Enter A or B: ")
    global list_EI
    global counterEIA
    global counterEIB
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_EI.append("A. Logical, thinking, questioning. ")

        counterEIA += 1
        fourth()
    elif user.casefold() == answer.casefold():
        list_EI.append("B. Empathetic, feeling, accommodating")

        counterEIB += 1
        fourth()
    else:
        print("""      
            Expected A or B as response
            I know this is an error, please try again
                        """)
        third()


def fourth():
    global list_EI
    print("4) A. Organized, orderly.          B. Flexible, adaptable.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_EI.append("A. Organized, orderly.")
        global counterEIA
        counterEIA += 1
        fifth()
    elif user.casefold() == answer.casefold():
        list_EI.append("B. Flexible, adaptable")
        global counterEIB
        counterEIB += 1
    else:
        print("""       Expected A or B as response
                        I know this is an error, please try again
                        """)
        fourth()


def fifth():
    global list_EI
    print("5) A. More outgoing, think out loud.           B. More reserved, think to yourself.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_EI.append("A. More outgoing, think out loud.")
        global counterEIA
        counterEIA += 1
        sixth()
    elif user.casefold() == answer.casefold():
        list_EI.append("B. More reserved, think to yourself.")
        global counterEIB
        counterEIB += 1
        sixth()
    else:
        print("""       Expected A or B as response
                        I know this is ans error, please try again
                        """)
        fifth()


def sixth():
    global list_SN
    print("6) A. Practical, realistic, experiential.          B. Imagination, innovative, theoretical.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_SN.append(" A. Practical, realistic, experiential.")
        global counterSNA
        counterSNA += 1
        seventh()
    elif user.casefold() == answer.casefold():
        list_SN.append("B. Imagination, innovative, theoretical.")
        global counterSNB
        counterSNB += 1
        seventh()
    else:
        print("""       Expected A or B as response
                        I know this is an error, please try again
                        """)
        sixth()


def seventh():
    global list_SN
    print(" 7) A. Candid, straight forward, frank.         B. Tactful, kind, encouraging.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_SN.append("A. Candid, straight forward, frank.")
        global counterSNA
        counterSNA += 1
        eight()
    elif user.casefold() == answer.casefold():
        list_SN.append("B. Tactful, kind, encouraging")
        global counterSNB
        counterSNB += 1
        eight()
    else:
        print("""       
                Expected A or B as response
                I know this is an error, please try again
                        """)
        seventh()


def eight():
    global list_SN
    print(" 8) A. Plan, schedule.          B. Unplanned, spontaneous\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_SN.append(" A. Plan, schedule")
        global counterSNA
        counterSNA += 1
        nine()
    elif user.casefold() == answer.casefold():
        list_SN.append("B. Unplanned, spontaneous ")
        global counterSNB
        counterSNB += 1
        nine()
    else:
        print("""
            Expected A or B as response
            print("I know this is an error, please try again
            """)
        eight()


def nine():
    global list_SN
    print("9) A. seek many tasks, public activities, interaction with others          B. seek private,"
          "solitary activities with quiet to concentrate.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_SN.append("A. seek many tasks, public activities, interaction with others ")
        global counterSNA
        counterSNA += 1
        ten()
    elif user.casefold() == answer.casefold():
        list_SN.append("B.seek private, solitary activities with quiet to concentrate  ")
        global counterSNB
        counterSNB += 1
        ten()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        nine()


def ten():
    global list_SN
    print("10) A. standard, usual, conventional.          B. different, novel, unique.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_SN.append("A. standard, usual, conventional.")
        global counterSNA
        counterSNA += 1
        eleven()
    elif user.casefold() == answer.casefold():
        list_EI.append(" B. different, novel, unique. ")
        global counterSNB
        counterSNB += 1
        eleven()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        ten()


def eleven():
    global list_JP
    print("11) A. firm, tend to criticize, hold the line.         B. gentle, tend to appreciate, conciliate. \n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_JP.append("A. firm, tend to criticize, hold the line.")
        global counterJPA
        counterJPA += 1
        twelve()
    elif user.casefold() == answer.casefold():
        list_JP.append("B. gentle, tend to appreciate, conciliate.")
        global counterJPB
        counterJPB += 1
        twelve()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        eleven()


def twelve():
    global list_JP
    print("12) A.regulated, structured.           B. easygoing, live e and let live.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_JP.append("A.regulated, structured.")
        global counterJPA
        counterJPA += 1
        thirteen()
    elif user.casefold() == answer.casefold():
        list_JP.append("B. easygoing, live e and let live")
        global counterJPB
        counterJPB += 1
        thirteen()
    else:
        print("""
            Expected A or B as response
            print("I know this is an error, please try again
        """)
        twelve()


def thirteen():
    global list_JP
    print("13) A. external, communicative, express yourself.          B. internal, reticent, keep to yourself.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_JP.append(" A. external, communicative, express yourself.")
        global counterJPA
        counterJPA += 1
        fourteen()
    elif user.casefold() == answer.casefold():
        list_JP.append("B. internal, reticent, keep to yourself.")
        global counterJPB
        counterJPB += 1
        fourteen()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        thirteen()


def fourteen():
    global list_JP
    print("14) A. focus on here-and-now.          B. look to the future, global perspective, big picture.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_JP.append("A. focus on here-and-now.")
        global counterJPA
        counterJPA += 1
        fifteen()
    elif user.casefold() == answer.casefold():
        list_EI.append(" B. look to the future, global perspective, big picture")
        global counterJPB
        counterJPB += 1
        fifteen()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        fourth()


def fifteen():
    global list_JP
    print("15) A. tough minded, just.         B. tender-hearted, merciful.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_JP.append("A. tough minded, just.")
        global counterJPA
        counterJPA += 1
        sixteen()
    elif user.casefold() == answer.casefold():
        list_JP.append("B. tender-hearted, merciful ")
        global counterJPB
        counterJPB += 1
        sixteen()
    else:
        print("""
            Expected A or B as response
            print("I know this is an error, please try again
            """)
        fifteen()


def sixteen():
    global list_TF
    print("16) A. preparation, plan ahead.            B. go with the flow, adapt as you go.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_TF.append("A. preparation, plan ahead.")
        global counterTFA
        counterTFA += 1
        seventeen()
    elif user.casefold() == answer.casefold():
        list_TF.append("B. go with the flow, adapt as you go ")
        global counterTFB
        counterTFB += 1
        seventeen()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        sixteen()


def seventeen():
    global list_TF
    print("17) A. active, initiate.       B. reflective, deliberate.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_TF.append("A. active, initiate ")
        global counterTFA
        counterTFA += 1
        eighteen()
    elif user.casefold() == answer.casefold():
        list_TF.append("B. reflective, deliberate")
        global counterTFB
        counterTFB += 1
        eighteen()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
        """)
        seventeen()


def eighteen():
    global list_TF
    print("18) A. facts, things, what is        B. ideas, dreams, 'what could be', philosophical.\n ")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_TF.append(" A. facts, things, what is ")
        global counterTFA
        counterTFA += 1
        nineteen()
    elif user.casefold() == answer.casefold():
        list_EI.append(" B. ideas, dreams, 'what could be', philosophical ")
        global counterTFB
        counterTFB += 1
        nineteen()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
        """)
        eighteen()


def nineteen():
    global list_TF
    print(" 19) A. matter of fact, issue oriented          B. sensitive, people-oriented, compassionate.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_TF.append(" 19) A. matter of fact, issue oriented ")
        global counterTFA
        counterTFA += 1
        twenty()
    elif user.casefold() == answer.casefold():
        list_TF.append(" B. sensitive, people-oriented, compassionate ")
        global counterTFB
        counterTFB += 1
        twenty()
    else:
        print("""
            Expected A or B as response
            I know this is an error, please try again
            """)
        nineteen()


def twenty():
    global list_TF
    print(" 20) A. control, govern         B. latitude, freedom.\n")
    user = input("Enter A or B: ")
    ans = "A"
    answer = "B"
    if user.casefold() == ans.casefold():
        list_TF.append("A. control, govern")
        global counterTFA
        counterTFA += 1
        answer()
    elif user.casefold() == answer.casefold():
        list_TF.append("B. latitude, freedom ")
        global counterTFB
        counterTFB += 1
        answer()
    else:
        print("""       
                Expected A or B as response
                I know this is an error, please try again
            """)
    twenty()


def answer():
    global user_name
    global list_EI
    global counterEIA
    global counterEIB

    print("\nHello" + user_name + "you selected")
    for i in list_EI:
        print(i)
    print(f"number of A selected:{counterEIA}")
    print(f"number of A selected:{counterEIB}")
    answer2()


def answer2():
    global list_SN
    global counterSNA
    global counterSNB
    for i in list_SN:
        print(i)
    print(f"number of A selected:{counterSNA}")
    print(f"number of A selected:{counterSNB}")
    answer3()


def answer3():
    global list_TF
    global counterTFA
    global counterTFB
    for i in list_TF:
        print(i)
    print(f"number of A selected:{counterTFA}")
    print(f"number of A selected:{counterTFB}")
    answer4()


def answer4():
    global list_JP
    global counterJPA
    global counterJPB
    for i in list_JP:
        print(i)
    print(f"number of A selected:{counterJPA}")
    print(f"number of A selected:{counterJPB}")
    personality()


def personality():
    global counterEIA
    global counterEIB
    global counterSNA
    global counterSNB
    global counterTFA
    global counterTFB
    global counterJPA
    global counterJPB
    global personalityOutput

    if counterEIA > counterEIB:
        personalityOutput += "E"
    else:
        personalityOutput += "I"

    if counterSNA > counterSNB:
        personalityOutput += "S"
    else:
        personalityOutput += "N"

    if counterTFA > counterTFB:
        personalityOutput += "T"
    else:
        personalityOutput += "F"

    if counterJPA > counterJPB:
        personalityOutput += "J"
    else:
        personalityOutput += "P"

    print("your personality is: " + personalityOutput)
    match personalityOutput:
        case "INFP":
            print("""
                    INFP stands for Introversion, iIntuition, Feeling, and Perceiving, which are four core 
                         personality traits. INFPs are energized by time alone (Introverted), focus on ideas and concepts rather 
                         than facts and details (intuitive), make decisions based on feelings and values (Feeling), and prefer to 
                         be spontaneous and flexible rather than planned. The INFP personality type is also called the "Healer" 
                         because of their sympathetic idealism and gentle compassion for other people. Other nicknames for the 
                         INFP include: INFPs are imaginative idealists, guided by their own core values and beliefs. To a Healer, 
                         possibilities are paramount; the realism of the moment is only of passing concern. They see potential 
                         for a better future, and pursue truth and meaning with their own individual flair. INFPs are sensitive, 
                         caring, and compassionate, and are deeply concerned with the personal growth of themselves and others. 
                         Individualistic and nonjudgmental, INFPs believe that each person must find their own path. They enjoy 
                         spending time exploring their own ideas and values, and are gently encouraging to others to do the same. 
                         INFPs are creative and often artistic; they enjoy finding new outlets for self-expression.
                         """)

        case "INFJ":
            print("""
                    INFJs are energized by time alone
                         intuitive: INFJs focus on ideas and concepts rather than facts and details
                         Feeling: INFJs make decisions based on feelings and values
                         Judging: INFJs prefer to be planned and organized rather than spontaneous and flexible

                     The INFJ personality type is also called the "Counselor" because of their tendency to be 
                     idealistic, compassionate, and sensitive. .INFJs are thoughtful nurturers with a strong sense of 
                     personal integrity and a drive to help others realize their potential. Creative and dedicated, 
                     they have a talent for helping others with original solutions to their personal challenges. They 
                     trust their insights about others and have strong faith in their ability to read people. 
                     Although they are sensitive, they are also reserved; the INFJ is a private sort, 
                     and is selective about sharing intimate thoughts and feelings.
                    """)

        case "ENFP":
            print("""
                    ENFP stands for Extroversion, intuition, Feeling, and Perceiving, which are four core 
                        personality traits. ENFPs are energized by time spent with others (Extraverted), focus on ideas and 
                        concepts rather than facts and details (iIntuitive), make decisions based on feelings and values (
                        Feeling), and prefer to be spontaneous and flexible rather than planned and organized (Perceiving). "The 
                        ENFP personality type is also called the Champion because of this type's enthusiasm for helping others 
                        realize their dreams. Other nicknames for the EN FP include:The Imaginative Motivator (MB-TI)" + "The 
                        Campaigner (16Personalities.
                    """)

        case "INTJ":
            print("""
                    INTJ stands for Introverted, iIntuitive, Thinking, Judging, which are four core personality 
                        traits. INTJs are energized by time alone (Introverted), focus on ideas and concepts rather than facts 
                        and details (iIntuitive), make decisions based on logic and reason (Thinking) and prefer to be planned 
                        and organized rather than spontaneous. INTJs are sometimes referred to as Mastermind personalities 
                        because of their strategic, logical way of thinking. Other nicknames for the INTJ include: INTJs are 
                        analytical problem-solvers, eager to improve systems and processes with their innovative ideas. They have 
                        a talent for seeing possibilities for improvement, whether at work, at home, or in themselves. Often 
                        intellectual, INTJs enjoy logical reasoning and complex problem-solving. They approach life by analyzing 
                        the theory behind what they see, and are typically focused inward, on their own thoughtful study of the 
                        world around them. INTJs are drawn to logical systems and are much less comfortable with the 
                        unpredictable nature of other people and their emotions. They are typically independent and selective 
                        about their relationships, preferring to associate with people who they find intellectually stimulating.
                    """)

        case "ENTJ":
            print("""
                ENTJ stands for Extraverted, iIntuitive, Thinking, Judging. ENTJ indicates a person who is 
                    energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts 
                    and details (iIntuitive), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    planned and organized rather than spontaneous and flexible (Judging). ENTJs are sometimes referred to as 
                    Commander personalities because of their innate drive to lead others.ENTJs are strategic leaders, 
                    motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, 
                    and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are 
                    usually articulate and quick-witted. ENTJs are analytical and objective, and like bringing order to the 
                    world around them. When there are flaws in a system, the ENTJ sees them, and enjoys the process of 
                    discovering and implementing a better way. ENTJs are assertive and enjoy taking charge; they see their 
                    role as that of leader and manager, organizing people and processes to achieve their goals.
                """)

        case "ENTP":
            print("""
                ENTP stands for Extraverted, iIntuitive, Thinking, Perceiving. ENTP indicates a person who is 
                    energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts 
                    and details (iNtuitive), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    spontaneous and flexible rather than planned and organized (Perceiving). ENTPs are sometimes referred to 
                    as Visionary personalities because of their passion for new, innovative ideas.ENTPs are inspired 
                    innovators, motivated to find new solutions to intellectually challenging problems. They are curious and 
                    clever, and seek to comprehend the people, systems, and principles that surround them. Open-minded and 
                    unconventional, Visionaries want to analyze, understand, and influence other people. ENTPs enjoy playing 
                    with ideas and especially like to banter with others. They use their quick wit and command of language to 
                    keep the upper hand with other people, often cheerfully poking fun at their habits and eccentricities. 
                    While the ENTP enjoys challenging others, in the end they are usually happy to live and let live. They 
                    are rarely judgmental, but they may have little patience for people who can('t keep up.' 
                """)
        case "INTP":
            print("""
                INTP stands for Introverted, Intuitive, Thinking, Perceiving.The INTP type describes a person 
                    who is energized by time alone (Introverted), who focuses on ideas and concepts rather than facts and 
                    details (iIntuitive), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    spontaneous and flexible rather than planned and organized (Perceiving). INTPs are sometimes referred to 
                    as Architect personalities because of their intuitive understanding of complex systems. Other nicknames 
                    for the INTP include:The Objective Analyst (MBTI).The Logician (16Personalities) INTPs are philosophical 
                    innovators, fascinated by logical analysis, systems, and design.They want to understand the unifying 
                    themes of life. INTPs are detached, analytical observers who can seem oblivious to the world around them 
                    because they are so deeply absorbed in thought. They spend much of their time in their own heads: 
                    exploring concepts, making connections, and seeking understanding of how things work. To the Architect, 
                    life is an ongoing inquiry into the mysteries of the universe.
                """)

        case "ESFJ":
            print("""
                ESFJ stands for Extraverted, Sensing, Feeling, Judging. ESFJ indicates a person who is 
                     energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas 
                     and concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be 
                     planned and organized rather than spontaneous and flexible (Judging). ESFJs are sometimes referred to as 
                     Provider personalities because of their interest in taking care of others in practical ways.ESFJs are 
                     conscientious helpers, sensitive to the needs of others and energetically dedicated to their 
                     responsibilities. They are highly attuned to their emotional environment and attentive to both the 
                     feelings of others and the perception others have of them. ESFJs like a sense of harmony and cooperation 
                     around them, and are eager to please and provide ESFJs value loyalty and tradition, and usually make 
                     their family and friends their top priority. They are generous with their time, effort, and emotions. 
                     They often take on the concerns of others as if they were their own, and will attempt to put their 
                     significant organizational talents to use to bring order to other people's lives.
                """)

        case "ESFP":
            print("""
                ESFP stands for Extraverted, Sensing, Feeling, Perceiving. ESFP indicates a person who is 
                    energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas and 
                    concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be 
                    spontaneous and flexible rather than planned and organized (Perceiving). ESFPs are sometimes referred to 
                    as Performer personalities because of their playful, energetic nature.ESFPs are vivacious entertainers 
                    who charm and engage those around them. They are spontaneous, energetic, and fun-loving, 
                    and take pleasure in the things around them: food, clothes, nature, animals, and especially people. ESFPs 
                    are typically warm and talkative and have a contagious enthusiasm for life. They like to be in the middle 
                    of the action and the center of attention. They have a playful, open sense of humor, and like to draw out 
                    other people and help them have a good time.
                """)

        case "ISFP":
            print("""
                ISFP stands for Introverted, Sensing, Feeling, Perceiving. ISFP indicates a person who is 
                     energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and 
                     concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be 
                     spontaneous and flexible rather than planned and organized (Perceiving). ISFPs are sometimes referred to 
                     as Composer personalities because of their innate sensibility for creating aesthetically pleasing 
                     experiences.ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with 
                     cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy 
                     what life has to offer. ISFPs are quiet and unassuming, and may be hard to get to know. However, 
                     to those who know them well, the ISFP is warm and friendly, eager to share in life's many experiences. 
                     ISFPs have a strong aesthetic sense and seek out beauty in their surroundings. They are attuned to 
                     sensory experience, and often have a natural talent for the arts. ISFPs especially excel at manipulating 
                     objects, and may wield creative tools like paintbrushes and sculptor's knives with great mastery.
                    """)

        case "ESTJ":
            print("""
                ESTJ stands for Extraverted, Sensing, Thinking, Judging. ESTJ indicates a person who is 
                    energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas and 
                    concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    planned and organized rather than spontaneous and flexible (Judging). ESTJs are sometimes referred to as 
                    Supervisor personalities because they tend to take charge and make sure things are done correctly. ESTJs 
                    are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, 
                    rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a 
                    systematic. ESTJs are the consummate organizers, and want to bring structure to their surroundings. They 
                    value predictability and prefer things to proceed in a logical order. When they see a lack of 
                    organization, the ESTJ often takes the initiative to establish processes and guidelines, so that everyone 
                    knows what's expected.
                """)

        case "ESTP":
            print("""
                ESTP stands for Extraverted, Sensing, Thinking, Perceiving. ESTP indicates a person who is 
                     energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas 
                     and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                     spontaneous and flexible rather than planned and organized (Perceiving) ESTPs are sometimes referred to 
                     as Dynamo personalities because of their high-energy, active approach to life. ESTPs are energetic 
                     thrill seekers who are at their best when putting out fires, whether literal or metaphorical. They bring 
                     a sense of dynamic energy to their interactions with others and the world around them. They assess 
                     situations quickly and move adeptly to respond to immediate problems with practical solutions. Active 
                     and playful, ESTPs are often the life of the party and have a good sense of humor. They use their keen 
                     powers of observation to assess their audience and adapt quickly to keep interactions exciting. Although 
                     they typically appear very social, they are rarely sensitive; the ESTP prefers to keep things fast-paced 
                     and silly rather than emotional or serious.
                """)

        case "ISTJ":
            print("""
                ISTJ stands for Introverted, Sensing, Thinking, Judging. ISTJ indicates a person who is 
                    energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and 
                    concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    planned and organized rather than spontaneous and flexible (Judging). ISTJs are sometimes referred to as 
                    Inspector personalities because of their focus on details and interest in doing things correctly.ISTJs 
                    are responsible organizers, driven to create and enforce order within systems and institutions. They are 
                    neat and orderly, inside and out, and tend to have a procedure for everything they do. Reliable and 
                    dutiful, ISTJs want to uphold tradition and follow regulations ISTJs are steady, productive contributors. 
                    Although they are Introverted, ISTJs are rarely isolated; typical ISTJs know just where they belong in 
                    life, and want to understand how they can participate in established organizations and systems. They 
                    concern themselves with maintaining the social order and making sure that standards are met.
                """)

        case "ISTP":
            print("""
                ISTP stands for Introverted, Sensing, Thinking, Perceiving. ISTP indicates a person who is 
                    energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and 
                    concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be 
                    spontaneous and flexible rather than planned and organized (Perceiving). ISTPs are sometimes referred to 
                    as Crafts person personalities because they typically have an innate mechanical ability and facility with 
                    tools.ISTPs are observant artisans with an understanding of mechanics and an interest in troubleshooting. 
                    They approach their environments with a flexible logic, looking for practical solutions to the problems 
                    at hand. They are independent and adaptable, and typically interact with the world around them in a 
                    self-directed, spontaneous manner. ISTPs are attentive to details and responsive to the demands of the 
                    world around them. Because of their astute sense of their environment, they are good at moving quickly 
                    and responding to emergencies. ISTPs are reserved, but not withdrawn: the ISTP enjoys taking action, 
                    and approaches the world with a keen appreciation for the physical and sensory experiences it has to 
                    offer.
                """)

        case "ENFJ":
            print("""
                ENFJ stands for Extraverted, iIntuitive, Feeling, Judging. ENFJ indicates a person who is 
                    energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts 
                    and details (iNtuitive), who makes decisions based on feelings and values (Feeling) and who prefers to be 
                    planned and organized rather than spontaneous and flexible (Judging). ENFJs are sometimes referred to as 
                    Teacher personalities because of their interest in helping others develop and grow.ENFJs are idealist 
                    organizers, driven to implement their vision of what is best for humanity. They often act as catalysts 
                    for human growth because of their ability to see potential in other people and their charisma in 
                    persuading others to their ideas. They are focused on values and vision, and are passionate about the 
                    possibilities for people. ENFJs are typically energetic and driven, and often have a lot on their plates. 
                    They are tuned into the needs of others and acutely aware of human suffering; however, they also tend to 
                    be optimistic and forward-thinking, intuitively seeing opportunity for improvement. The ENFJ is 
                    ambitious, but their ambition is not self-serving: rather, they feel personally responsible for making 
                    the world a better place.
                """)

        case "ISFJ":
            print("""
                It stands for Introverted, Sensing, Feeling, Judging. ISFJ indicates a person who is energized 
                    by time spent alone (Introverted), who focuses on facts and details rather than ideas and concepts (
                    Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be planned and 
                    organized rather than spontaneous and flexible (Judging). ISFJs are sometimes referred to as Protector 
                    personalities because of their interest in keeping people safe and well cared for.ISFJs are industrious 
                    caretakers, loyal to traditions and organizations. "They are practical, compassionate, and caring, 
                    and are motivated to provide for others and protect them from the perils of life. "ISFJs are conventional 
                    and grounded, and enjoy contributing to established structures of society. They are steady and committed 
                    workers with a deep sense of responsibility to others. They focus on fulfilling their duties, 
                    particularly when they are taking care of the needs of other people. They want others to know that they 
                    are reliable and can be trusted to do what is expected of them. They are conscientious and methodical, 
                    and persist until the job is done.
                """)
        case _:
            print("Your personality is unknown")


if __name__ == "__main__":
    print(first())
