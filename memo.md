# todo
- foliumでそれぞれの街がどこにあるのか表示できそう
- それに応じて天気を表示できると面白そう
<!-- - こいつやっぱりレスポンシブのことあまり考えてなさそう -->
<!-- - そしてもしかしてfolium使えば水滸伝地図が作れるんじゃないか -->
- １．日本地図全体を表示して、主要な都市にアイコンを立てる
- ２．任意のアイコンをクリックするとその地図を拡大する
- ３．地図周辺の都市の天気を表示する
- たぶんこのくらいなら出来そう。
- ４．最終的にはflaskでhtml出力すれば出来るっぽい？ってことはreactとか使わずに行ける？？
<!-- - 今回もフロント側の練習にならないんじゃないのかそれ -->

## これからの指針
- [x] 取得したい都市の選定...ざっくり地方ごとに一つずつ都市をピックアップ。稚内、札幌、仙台、新潟、東京、金沢、長野、大阪、福山、高知、福岡、鹿児島、那覇
- [x] 都市名（英語表記）、都市名（漢字表記…これどうリンクしようか）、ロケーション（lat, lon）をまとめてオブジェクト化
- 　→　このまとまりそのものをクラス化した方がいいのかも？？
- [ ] OpenWeatherのAPIで都市別の天気情報を取得。毎回とるとダルいので、例えばサイト接続時に一回だけとる、みたいな感じ。

## 都市の気象情報として何を取得するか
- アイコン ... [weather][icon] ... https://openweathermap.org/img/wn/{icon}@2x.png ... {icon}のところを変えるとアイコンを取得できそう
- 現在の天気 ... [weather][description]
- 体感気温 ... [main][feels_like]
- 湿度 ... [main][humidity]
- 海面気圧 ... [main][sea_level] ... 天気予報などで用いられる、現地の高低差を馴らした気圧
- 地表面気圧 ... [main][grnd_level] ... 体感的な気圧

## leafletのアイコンの種類：
- アイコンをいじりたい場合はここを見ると参考になるかも？
- https://github.com/lennardv2/Leaflet.awesome-markers#icons
- アイコン名はデフォルトだとBootstrap Glyphicons, prefix="fa"だとfont awesomeから来ているらしい
- font awesomeのほうが少し丸みがあってポップなデザイン
- https://fontawesome.com/v4/icons/
- https://getbootstrap.com/docs/3.3/components/#glyphicons