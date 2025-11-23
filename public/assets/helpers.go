package helpers

import (
	"crypto/rand"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

// GenerateRandomString generates a random string of a given length.
func GenerateRandomString(length int) (string, error) {
	if length <= 0 {
		return "", errors.New("length must be greater than 0")
	}

	b := make([]byte, length)
	_, err := rand.Read(b)
	if err != nil {
		return "", err
	}

	return hex.EncodeToString(b), nil
}

// FileExists checks if a file exists at the given path.
func FileExists(path string) bool {
	if _, err := os.Stat(path); errors.Is(err, os.ErrNotExist) {
		return false
	}
	return true
}

// EnsureDir checks if a directory exists, and if not, creates it.
func EnsureDir(dirPath string) error {
	if !FileExists(dirPath) {
		return os.MkdirAll(dirPath, os.ModePerm)
	}
	return nil
}

// CopyFile copies a file from src to dst.
func CopyFile(src, dst string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destFile.Close()

	_, err = io.Copy(destFile, sourceFile)
	if err != nil {
		return err
	}

	return nil
}

// GetFileExtension returns the file extension from a given path.
func GetFileExtension(path string) string {
	return strings.ToLower(filepath.Ext(path))
}

// RemoveFile removes a file at the given path.
func RemoveFile(path string) error {
	if !FileExists(path) {
		return fmt.Errorf("file does not exist: %s", path)
	}
	return os.Remove(path)
}

// ReadFile reads the content of a file and returns it as a string.
func ReadFile(path string) (string, error) {
	if !FileExists(path) {
		return "", fmt.Errorf("file does not exist: %s", path)
	}

	data, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}

	return string(data), nil
}

// WriteFile writes content to a file at the given path.
func WriteFile(path, content string) error {
	return os.WriteFile(path, []byte(content), os.ModePerm)
}