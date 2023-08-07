import streamlit as st
import requests

APIURL = "https://api.github.com/users/"

def get_user_data(username):
    resp = requests.get(APIURL + username)
    resp_data = resp.json()
    return resp_data

def get_repos_data(username):
    resp = requests.get(APIURL + username + '/repos')
    resp_data = resp.json()
    return resp_data

def main():
    st.set_page_config(
        page_title="Github User",
        page_icon=":octocat:",
        layout="centered"
    )

    st.markdown(
        """
        <style>
        body {
            background-image: url('bg.gif');
            background-size: cover;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: "Poppins", sans-serif;
            margin: 0;
            min-height: 100vh;
        }
        input[type="text"] {
            background-color: #4c2885;
            border-radius: 10px;
            border: none;
            color: white;
            font-family: inherit;
            font-size: 1rem;
            padding: 1rem;
            margin-bottom: 2rem;
        }
        input::placeholder {
            color: #bbb;
        }
        .card {
            background-color: #4c2885;
            background-image: linear-gradient(315deg,  #4c2885  0%, #4c11ac 100%);
            border-radius: 20px;
            box-shadow: 0 5px 10px rgba(154, 160, 185, .0) , 0 15px 40px rgba(0 ,0 ,0 ,.1);
            display: flex;
            padding: 3rem;
            max-width: 800px;
        }
        .avatar {
            border: 10px solid #2a2a72;
            border-radius: 50%;
            height: 150px;
            width: 150px;
        }
        .user-info {
            color: #eee;
            margin-left: 2rem;
        }
        .user-info h2 {
            margin-top: 0;
        }
        .user-info ul {
            display: flex;
            justify-content: space-between;
            list-style-type: none;
            padding: 0;
            max-width: 400px;
        }
        .user-info ul li {
            display: flex;
            align-items: center;
        }
        .user-info ul li strong {
            font-size: 0.9rem;
            margin-left: 0.5rem;
        }
        .repo {
            background-color: #2a2a72;
            border-radius: 5px;
            display: inline-block;
            color: white;
            font-size: 0.7rem;
            padding: 0.25rem 0.5rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Github User Search")

    username = st.text_input("Enter a GitHub username:")
    
    if st.button("Search"):
        if username:
            user_data = get_user_data(username)
            repos_data = get_repos_data(username)

            st.subheader("User Information")
            st.image(user_data['avatar_url'], caption=user_data['name'], use_column_width=True)
            st.write(user_data['bio'])
            st.write(f"Followers: {user_data['followers']}, Following: {user_data['following']}, Repos: {user_data['public_repos']}")

            st.subheader("Top Repositories")
            repos = sorted(repos_data, key=lambda repo: repo['stargazers_count'], reverse=True)[:10]
            for repo in repos:
                st.markdown(f"[{repo['name']}]({repo['html_url']}) - Stars: {repo['stargazers_count']}", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
