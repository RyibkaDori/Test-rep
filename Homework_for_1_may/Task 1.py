import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def load_audio(file_path):
    data, sample_rate = sf.read(file_path)
    if len(data.shape) > 1:
        data = data[:, 0]
    return sample_rate, data.astype(np.float64)


def save_audio(file_path, sample_rate, data):
    sf.write(file_path, data, sample_rate)


def main():
    sample_rate, audio = load_audio('02_Suyano_amp_Wasback_feat_Daimy_Lotus_-_Colors_Radio_Edit.wav')
    print(f"Частота: {sample_rate} Гц, Длина: {len(audio)}")
    print(f"Длительность: {len(audio) / sample_rate:.2f} сек")

    original_length = len(audio)
    size = 2 ** int(np.ceil(np.log2(original_length)))
    print(f"Размер после дополнения: {size}")

    padded = np.zeros(size, dtype=complex)
    padded[:original_length] = audio

    spectrum = np.fft.fft(padded)
    spectrum_shifted = np.fft.fftshift(spectrum)

    mask_percent = 0.2
    center = size // 2
    radius = int(size * mask_percent / 2)
    mask = np.zeros(size, dtype=complex)
    mask[center - radius: center + radius] = 1

    filtered_spectrum = spectrum_shifted * mask

    reconstructed = np.real(np.fft.ifft(np.fft.ifftshift(filtered_spectrum)))
    reconstructed = reconstructed[:original_length]

    save_audio('filtered.wav', sample_rate, reconstructed)
    print("Сохранено в filtered.wav")

    freqs_padded = np.fft.fftfreq(size, 1 / sample_rate)

    plt.figure(figsize=(12, 10))

    plt.subplot(2, 1, 1)
    plt.plot(np.fft.fftshift(freqs_padded), np.abs(np.fft.fftshift(spectrum)))
    plt.title('Исходный спектр')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, sample_rate // 2)
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 1, 2)
    reconstructed_padded = np.zeros(size, dtype=complex)
    reconstructed_padded[:original_length] = reconstructed
    filtered_fft = np.fft.fft(reconstructed_padded)
    plt.plot(np.fft.fftshift(freqs_padded), np.abs(np.fft.fftshift(filtered_fft)))
    plt.title(f'Отфильтрованный спектр ({int(mask_percent * 100)}% частот)')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, sample_rate // 2)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()



main()