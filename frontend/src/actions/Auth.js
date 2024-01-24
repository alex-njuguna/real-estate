import axios from "axios";
import { setAlert } from "./Alert";
import {
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  SIGNUP_SUCCESS,
  SIGNUP_FAIL,
  LOGOUT,
} from "./types";

export const login = (email, password) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const body = JSON.stringify({ email, password });

  try {
    const response = await axios.post(
      "http://localhost:8000/api/token/",
      body,
      config
    );

    dispatch({
      type: LOGIN_SUCCESS,
      payload: response.data,
    });

    dispatch(setAlert("Authenticated successfully", "success"));
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL,
    });

    dispatch(setAlert("Error Authenticating", "error"));
  }
};

export const signup =
  ({ name, email, password, password2 }) =>
  async (dispatch) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const body = JSON.stringify({ name, email, password, password2 });

    try {
      const response = await axios.post(
        "http://localhost:8000/api/accounts/signup/",
        body,
        config
      );

      dispatch({
        type: SIGNUP_SUCCESS,
        payload: response.data,
      });

      dispatch(login(email, password));
    } catch (err) {
      dispatch({
        type: SIGNUP_FAIL,
      });

      dispatch(setAlert("Error Creating account", "error"));
    }
  };
