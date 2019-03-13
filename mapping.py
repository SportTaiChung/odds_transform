
def bsMap (water) :
    oddsmap = {
            0.95: "1+95",
            0.9: "1+90",
            0.85: "1+85",
            0.8: "1+80",
            0.75: "1+75",
            0.7: "1+70",
            0.65: "1+65",
            0.6: "1+60",
            0.55: "1+55",
            0.5: "1+50",
            0.45: "1+45",
            0.4: "1+40",
            0.35: "1+35",
            0.3: "1+30",
            0.25: "1+25",
            0.2: "1+20",
            0.15: "1+15",
            0.1: "1+10",
            0.05: "1+5",
            0.0: "1+0",
            -0.05: "1-5",
            -0.1: "1-10",
            -0.15: "1-15",
            -0.2: "1-20",
            -0.25: "1-25",
            -0.3: "1-30",
            -0.35: "1-35",
            -0.4: "1-40",
            -0.45: "1-45",
            -0.5: "1-50",
            -0.55: "1-55",
            -0.6: "1-60",
            -0.65: "1-65",
            -0.7: "1-70",
            -0.75: "1-75",
            -0.8: "1-80",
            -0.85: "1-85",
            -0.9: "1-90",
            -0.95:"1-95",
            -1.0: "1-100",
            -1.05: "2+95",
            -1.1: "2+90",
            -1.15: "2+85",
            -1.2: "2+80",
            -1.25: "2+75",
            -1.3: "2+70",
            -1.35: "2+65",
            -1.4: "2+60",
            -1.45: "2+55",
            -1.5: "2+50",
            -1.55: "2+45",
            -1.6: "2+40",
            -1.65: "2+35",
            -1.7: "2+30",
            -1.75: "2+25",
            -1.8: "2+20",
            -1.85: "2+15",
            -1.9: "2+10",
            -1.95: "2+5",
            -2.0: "2+0",
            -2.05: "2-5",
            -2.1: "2-10",
            -2.15: "2-15",
            -2.2: "2-20",
            -2.25: "2-25",
            -2.3: "2-30",
            -2.35: "2-35",
            -2.4: "2-40",
            -2.45: "2-45",
            -2.5: "2-50",
            -2.55: "2-55",
            -2.6: "2-60",
            -2.65: "2-65",
            -2.7: "2-70",
            -2.75: "2-75",
            -2.8: "2-80",
            -2.85: "2-85",
            -2.9: "2-90",
            -2.95:"2-95",
            -3.0: "2-100",
        }
    return oddsmap[water]

def hcMap (water) :
    oddsmap = {
            2.0: "0",
            1.95: "0-5",
            1.9: "0-10",
            1.95: "0-15",
            1.8: "0-20",
            1.75: "0-25",
            1.65: "0-35",
            1.6: "0-40",
            1.55: "0-45",
            1.5: "0-50",
            1.45: "0-55",
            1.4: "0-60",
            1.35: "0-65",
            1.3: "0-70",
            1.25: "0-75",
            1.2: "0-80",
            1.15: "0-85",
            1.1: "0-90",
            1.05: "0-95",
            1: "0-100",
            0.95: "1+95",
            0.9: "1+90",
            0.85: "1+85",
            0.8: "1+80",
            0.75: "1+75",
            0.7: "1+70",
            0.65: "1+65",
            0.6: "1+60",
            0.55: "1+55",
            0.5: "1+50",
            0.45: "1+45",
            0.4: "1+40",
            0.35: "1+35",
            0.3: "1+30",
            0.25: "1+25",
            0.2: "1+20",
            0.15: "1+15",
            0.1: "1+10",
            0.05: "1+5",
            0.0: "1+0",
            -0.05: "1-5",
            -0.1: "1-10",
            -0.15: "1-15",
            -0.2: "1-20",
            -0.25: "1-25",
            -0.3: "1-30",
            -0.35: "1-35",
            -0.4: "1-40",
            -0.45: "1-45",
            -0.5: "1-50",
            -0.55: "1-55",
            -0.6: "1-60",
            -0.65: "1-65",
            -0.7: "1-70",
            -0.75: "1-75",
            -0.8: "1-80",
            -0.85: "1-85",
            -0.9: "1-90",
            -0.95:"1-95",
            -1.0: "1-100",
            -1.05: "2+95",
            -1.1: "2+90",
            -1.15: "2+85",
            -1.2: "2+80",
            -1.25: "2+75",
            -1.3: "2+70",
            -1.35: "2+65",
            -1.4: "2+60",
            -1.45: "2+55",
            -1.5: "2+50",
            -1.55: "2+45",
            -1.6: "2+40",
            -1.65: "2+35",
            -1.7: "2+30",
            -1.75: "2+25",
            -1.8: "2+20",
            -1.85: "2+15",
            -1.9: "2+10",
            -1.95: "2+5",
            -2.0: "2+0",
            -2.05: "2-5",
            -2.1: "2-10",
            -2.15: "2-15",
            -2.2: "2-20",
            -2.25: "2-25",
            -2.3: "2-30",
            -2.35: "2-35",
            -2.4: "2-40",
            -2.45: "2-45",
            -2.5: "2-50",
            -2.55: "2-55",
            -2.6: "2-60",
            -2.65: "2-65",
            -2.7: "2-70",
            -2.75: "2-75",
            -2.8: "2-80",
            -2.85: "2-85",
            -2.9: "2-90",
            -2.95:"2-95",
            -3.0: "2-100",
        }
    return oddsmap[water]



def bkMap (move) :
    moveMap = {
            19: "+75",
            18: "+50",
            17: "+25",
            16: "+0",
            15: "-25",
            14: "-50",
            13: "-75",
            12: "-100",
            11: "+75",
            10: "+50",
            9: "+25",
            8: "+0",
            7: "-25",
            6: "-50",
            5: "-75",
            4: "-100",
            3: "+75",
            2: "+50",
            1: "+25",
            0: "+0",
            -1: "-25",
            -2: "-50",
            -3: "-75",
            -4: "-100",
            -5: "+75",
            -6: "+50",
            -7: "+25",
            -8: "+0",
            -9: "-25",
            -10: "-50",
            -11: "-75",
            -12: "-100",
            -13: "+75",
            -14: "+50",
            -15: "+25",
            -16: "+0",
            -17: "-25",
            -18: "-50",
            -19: "-75",
            -20: "-100",
            }
    return moveMap[move]



def scMap(line):
    line = float(line)
    scmap = {
        0.0: "0.0",
        0.25: "0/0.5",
        0.5: "0.5",
        0.75: "0.5/1",
        1.0: "1.0",
        1.25: "1/1.5",
        1.5: "1.5",
        1.75: "1.5/2",
        2.0: "2",
        2.25: "2/2.5",
        2.5: "2.5",
        2.75: "2.5/3",
        3.0: "3.0",
        3.25: "3/3.5",
        3.5: "3.5",
        3.75: "3.5/4",
        4.0: "4.0",
        4.25: "4/4.5",
        4.5: "4.5",
        4.75: "4.5/5",
        5.0: "5.0",
        5.25: "5/5.5",
        5.5: "5.5",
        5.75: "5.5/6",
        6.0: "6.0",
        6.25: "6/6.5",
        6.5: "6.5",
        6.75: "6.5/7",
        7.0: "7.0",
        7.25: "7/7.5",
        7.5: "7.5",
        7.75: "7.5/8",
        8.0: "8.0",
        8.25: "8/8.5",
        8.5: "8.5",
        8.75: "8.5/9",
        9.0: "9.0",
        9.25: "9/9.5",
        9.5: "9.5",
        9.75: "9.5/10",
        10: "10.0",
        10.25: "10/10.5",
        10.5: "10.5",
        10.75: "10.5/11",
        11.0: "11.0",
        11.25: "11/11.5",
        11.5: "11.5",
        11.75: "11.5/12",
        12.0: "12.0",
        12.25: "12/12.5",
        12.5: "12.5",
        12.75: "12.5/13",
        13.0: "13.0",
        13.25: "13/13.5",
        13.5: "13.5",
        13.75: "13.5/14",
        14.0: "14.0",
        14.25: "14/14.5",
        14.5: "14.5",
        14.75: "14.5/15",
        15.0: "15.0",
        15.25: "15/15.5",
        15.5: "15.5",
        15.75: "15.5/16",
        16.0: "16.0",
        16.25: "16/16.5",
        16.5: "16.5",
        16.75: "16.5/17",
        17.0: "17.0",
        17.25: "17/17.5",
        17.5: "17.5",
        17.75: "17.5/18",
        18.0: "18.0",
        18.25: "18/18.5",
        18.5: "18.5",
        18.75: "18.5/19",
        19.0: "19.0",
        19.25: "19/19.5",
        19.5: "19.5",
        19.75: "19.5/20",
        20.0: "20.0",
        20.25: "20/20.5",
        20.5: "20.5",
        20.75: "20.5/21",
        21.0: "21.0",
        21.25: "21/21.5",
        21.5: "21.5",
        21.75: "21.5/21",
        22.0: "22.0",
        22.25: "22/22.5",
        22.5: "22.5",
        22.75: "22.5/23",
        23.0: "23.0",
        23.25: "23/23.5",
        23.5: "23.5",
        23.75: "23.5/24",
        24.0: "24.0",
        24.25: "24/24.5",
        24.5: "24.5",
        24.75: "24.5/25"

    }

    newLine = scmap[line]

    return newLine

def bsDeMap (percent) :
    oddsmap = {
            0.95: "1+5",
            0.9: "1+10",
            0.85: "1+15",
            0.8: "1+20",
            0.75: "1+25",
            0.7: "1+30",
            0.65: "1+35",
            0.6: "1+40",
            0.55: "1+45",
            0.5: "1+50",
            0.45: "1+55",
            0.4: "1+60",
            0.35: "1+65",
            0.3: "1+70",
            0.25: "1+75",
            0.2: "1+80",
            0.15: "1+85",
            0.1: "1+90",
            0.05: "1+95",
            0.0: "0+0",
            1.05: "1-5",
            1.1: "1-10",
            1.15: "1-15",
            1.2: "1-20",
            1.25: "1-25",
            1.3: "1-30",
            1.35: "1-35",
            1.4: "1-40",
            1.45: "1-45",
            1.5: "1-50",
            1.55: "1-55",
            1.6: "1-60",
            1.65: "1-65",
            1.7: "1-70",
            1.75: "1-75",
            1.8: "1-80",
            1.85: "1-85",
            1.9: "1-90",
            1.95:"1-95",
            2.0: "1-100",
            2.05: "2+95",
            2.1: "2+90",
            2.15: "2+85",
            2.2: "2+80",
            2.25: "2+75",
            2.3: "2+70",
            2.35: "2+65",
            2.4: "2+60",
            2.45: "2+55",
            2.5: "2+50",
            2.55: "2+45",
            2.6: "2+40",
            2.65: "2+35",
            2.7: "2+30",
            2.75: "2+25",
            2.8: "2+20",
            2.85: "2+15",
            2.9: "2+10",
            2.95: "2+5",
            3.0: "2+0",
            3.05: "2-5",
            3.1: "2-10",
            3.15: "2-15",
            3.2: "2-20",
            3.25: "2-25",
            3.3: "2-30",
            3.35: "2-35",
            3.4: "2-40",
            3.45: "2-45",
            3.5: "2-50",
            3.55: "2-55",
            3.6: "2-60",
            3.65: "2-65",
            3.7: "2-70",
            3.75: "2-75",
            3.8: "2-80",
            3.85: "2-85",
            3.9: "2-90",
            3.95:"2-95",
            4.0: "2-100",
        }
    return oddsmap[percent]