from flask import Flask
from flask_cors import CORS
import speedtest

app = Flask(__name__)

CORS(app)

@app.route('/speed-test')
def testspeed():
    st = speedtest.Speedtest()

    st.get_best_server()

    st.download() 

    st.upload() 

    res_dict = st.results.dict()

    dwnl = str(res_dict['download'])[:2] + "." + \
        str(res_dict['download'])[2:4]

    upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]

    result = {
        "download": f"{dwnl}mbps({float(dwnl)*0.125:.2f}MBs)",
        "upload": f"{upl}mbps ({float(upl)*0.125:.2f}MBs)",
        "ping": f"{res_dict['ping']:.2f}ms",
        "host": f"{res_dict['server']['host']}",
        "sponsor": f"{res_dict['server']['sponsor']}",
        "latency": f"{res_dict['server']['latency']:.2f}"
    }

    return result

if __name__ == '__main__':
    app.run(debug=True)
