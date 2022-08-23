# https://forms.office.com/Pages/ResponsePage.aspx?id=skPpVutfMUa0cQNGQMsYbGpXnkvNOxxPlw82yuB56QdURUZTVVFIRkZWTkRBUEhUTktMSk84M1RFQS4u&qrcode=true

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.keys import Keys
# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import psycopg2
import psycopg2.extras
import pandas as pd
from sqlalchemy import create_engine

# バグ対策
import numpy as np
from psycopg2.extensions import register_adapter, AsIs


def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)


def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


def addapt_numpy_float32(numpy_float32):
    return AsIs(numpy_float32)


def addapt_numpy_int32(numpy_int32):
    return AsIs(numpy_int32)


def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))


register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)
register_adapter(np.float32, addapt_numpy_float32)
register_adapter(np.int32, addapt_numpy_int32)
register_adapter(np.ndarray, addapt_numpy_array)


def enter_kekou_kansatu(wait, class_number, student_number, student_name, body_temperature):

    # 入力欄をクリック
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input[1]")))
    search_box.click()
    # 今日の日付ボタンをクリック
    picker_button_today = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[1]")))
    picker_button_today.click()
    # クラス欄をクリック
    select_placeholder_class_number = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div")))
    select_placeholder_class_number.click()
    # クラス入力
    class_number_xpath = f"/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[{class_number}]"
    enter_name = wait.until(EC.element_to_be_clickable((By.XPATH, class_number_xpath)))
    enter_name.click()
    # 出席番号欄をクリック
    select_placeholder_student_number = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div")))
    select_placeholder_student_number.click()
    # 出席番号入力
    student_number_xpath = f"/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[{student_number}]"
    enter_student_number = wait.until(EC.element_to_be_clickable((By.XPATH, student_number_xpath)))
    enter_student_number.click()
    # 名前入力
    name_enter = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div/input")))
    name_enter.click()
    name_enter.send_keys(student_name)
    # 体温入力
    enter_body_temperature = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div/input")))
    enter_body_temperature.click()
    enter_body_temperature.send_keys(body_temperature)
    # 症状入力
    enter_no_symptom = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input")))
    enter_no_symptom.click()


def send_line_notify_message(notification_message):
    """
    LINEにメッセージを送る
    """
    # herokuに設定した環境変数"LINE_NOTIFY_TOKEN"からアクセストークンを持ってくる
    LINE_TOKEN = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f"{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


def send_line_notify_image(notification_message, image):
    """
    LINEにメッセージ&画像を送る
    """
    LINE_TOKEN = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f"{notification_message}"}
    # rbはバイナリファイルを読み取りモードで開くオプション
    files = {"imageFile": open(image, "rb")}
    requests.post(line_notify_api, headers=headers, data=data, files=files)


def datetime_to_str():
    """
    日時の取得&str型に変換
    """
    datetime_first = datetime.datetime.now()
    datetime_str = datetime_first.strftime("%Y-%m-%d %H:%M:%S")

    return datetime_str


def get_connection():
    connection_config = {
        'user': os.environ.get("connection_config_user"),
        'password': os.environ.get("connection_config_password"),
        'host': os.environ.get("connection_config_host"),
        'port': os.environ.get("connection_config_port"),
        'database': os.environ.get("connection_config_database"),
    }
    conn = psycopg2.connect(**connection_config)
    return conn


def get_connection_with_engine():
    connection_config = {
        'user': os.environ.get("connection_config_user"),
        'password': os.environ.get("connection_config_password"),
        'host': os.environ.get("connection_config_host"),
        'port': os.environ.get("connection_config_port"),
        'database': os.environ.get("connection_config_database"),
    }
    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))
    return engine


def sql_to_df(table):
    with get_connection() as conn:
        with conn.cursor() as cur:
            conn.cursor_factory = psycopg2.extras.DictCursor
            sql = f'SELECT * FROM {table}'
            cur.execute(sql)
            data_frame_from_postqresql = pd.read_sql(sql, conn)
            return data_frame_from_postqresql


def call_df_len(table):
    call_df = sql_to_df(table)
    call_df_length = len(call_df)
    return call_df_length


def call_sql_to_df(wait, table, i):
    call_df = sql_to_df(table)
    try:
        call_df_series_row = call_df.loc[i]
    except KeyError:
        print("KeyError")

    else:
        user_info_grade_number = call_df_series_row["user_info_grade_number"]
        class_number = call_df_series_row["user_info_class_number"]
        student_number = call_df_series_row["user_info_student_number"]
        student_name = call_df_series_row["user_info_student_name"]
        body_temperature = call_df_series_row["user_info_body_temperature"]
        is_run_code = call_df_series_row["is_run_code"]

        engine = get_connection_with_engine()

        if is_run_code == 1:
            if user_info_grade_number == 3:
                enter_kekou_kansatu(wait, class_number, student_number, student_name, body_temperature)
                call_df_series_row["user_info_last_run_at"] = datetime_to_str()

                call_df_dataFrame = pd.DataFrame(call_df_series_row)  # pandas.Seriesだとバグるのでpandas.DataFrameに変更
                npd_T = call_df_dataFrame.T  # 行と列をひっくり返す

                with get_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(f'DROP TABLE {table}')
                npd_T.to_sql(table, engine, if_exists='replace', index=True, method='multi', chunksize=1000)

            elif user_info_grade_number == 2:
                print("2年生")
            elif user_info_grade_number == 1:
                print("1年生")

        elif is_run_code == 0:
            print("実行しない")
        else:
            print(f"is_run_code_eroor_{i}回目")


def main():

    table = "users_userinfo"
    call_df_length = call_df_len(table)

    for i in range(0, call_df_length):
        # for i in range(0, 3):

        count = i+1
        # chrome_path = r'D:\chromedriver_win32\chromedriver.exe'
        chrome_path = '/app/.chromedriver/bin/chromedriver'
        options = Options()
        options.add_argument('--incognito')
        options.set_headless()  # ブラウザ非表示で実行
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        # driver.implicitly_wait(30)

        url = "https://forms.office.com/Pages/ResponsePage.aspx?id=skPpVutfMUa0cQNGQMsYbGpXnkvNOxxPlw82yuB56QdURUZTVVFIRkZWTkRBUEhUTktMSk84M1RFQS4u&qrcode=true"
        driver.get(url)
        # 最大の読み込み時間を設定 今回は最大30秒待機できるようにする
        wait = WebDriverWait(driver=driver, timeout=30)

        call_sql_to_df(wait, table, i)

        # ページ全体のスクショを撮るためのおまじない
        # page_width = driver.execute_script("return document.body.scrollWidth")
        # page_height = driver.execute_script("return document.body.scrollHeight")
        # driver.set_window_size(page_width, page_height)
        # 送信ボタンをクリックする前のスクリーンショットを撮影
        # driver.save_screenshot("before.png")

        # 送信ボタンをクリック
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div")))
        send_button.click()

        # 正常に動作したかどうか確認
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/span")))
        except TimeoutException:
            print("なし")
        finally:
            print(f"{count}回目 正常に動作しました")

        # 送信ボタンをクリックした後のスクリーンショットを撮影
        # driver.save_screenshot("after.png")

        print("Done " + datetime_to_str())

        # LINE送信
        # send_line_notify_image("before", "before.png")
        # send_line_notify_image("after", "after.png")

        send_line_notify_message(f"\n{count}回目 提出しました\n" + datetime_to_str())

        driver.quit()


if __name__ == "__main__":
    main()


# https://tanuhack.com/pandas-postgres-readto/#PostgreSQL
